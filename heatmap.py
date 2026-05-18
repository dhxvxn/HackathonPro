import cv2
import numpy as np
import sqlite3
from typing import Optional, List, Tuple
from db_schema import get_db_path

def generate_heatmap(
    video_path: str,
    camera_id: Optional[int] = None,
    global_id: Optional[int] = None,
    output_path: str = "heatmap.jpg"
) -> bool:
    """
    Generates a movement heatmap based on tracking data.
    """
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sql = """
        SELECT bbox_x1, bbox_y1, bbox_x2, bbox_y2
        FROM tracking_data
        WHERE video_path = ?
    """
    params = [video_path]

    if camera_id is not None:
        sql += " AND camera_id = ?"
        params.append(camera_id)
    if global_id is not None:
        sql += " AND global_id = ?"
        params.append(global_id)

    cursor.execute(sql, params)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No tracking data found for heatmap generation.")
        return False

    # Get video dimensions from the first frame of the video
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        print(f"Could not open video {video_path} for heatmap background.")
        cap.release()
        return False
    
    height, width = frame.shape[:2]
    accum_mask = np.zeros((height, width), dtype=np.float32)

    for x1, y1, x2, y2 in rows:
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        # Draw a small "heat" point
        cv2.circle(accum_mask, (cx, cy), 15, (1.0), -1)

    # Blur the accumulation mask to make it look like a heatmap
    accum_mask = cv2.GaussianBlur(accum_mask, (51, 51), 0)

    # Normalize
    cv2.normalize(accum_mask, accum_mask, 0, 255, cv2.NORM_MINMAX)
    accum_mask = accum_mask.astype(np.uint8)

    # Apply colormap
    heatmap_img = cv2.applyColorMap(accum_mask, cv2.COLORMAP_JET)

    # Blend with original frame
    result = cv2.addWeighted(frame, 0.6, heatmap_img, 0.4, 0)

    cv2.imwrite(output_path, result)
    print(f"Heatmap saved to {output_path}")
    cap.release()
    return True
