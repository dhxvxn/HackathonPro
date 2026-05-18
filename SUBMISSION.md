# Hackathon MVP Submission: Smart CCTV AI

## 🎥 Project Overview
Smart CCTV AI is an intelligent surveillance system that transforms traditional CCTV footage into a searchable, metadata-indexed database. It allows users to query events using natural language (e.g., "person near gate") and retrieve relevant video segments instantly without re-processing the entire feed.

---

## 🏗 Architecture Overview

The system follows a modular pipeline designed for real-time efficiency and cross-camera consistency:

1.  **Ingestion & Detection:** Video feeds are processed using **YOLOv8** for high-speed object detection.
2.  **Tracking:** **DeepSORT** maintains local identities within a single camera view.
3.  **Identity Matching (ReID):** A custom **Two-Stage Global ID Manager** extracts feature embeddings and shirt colors to maintain identity across multiple cameras, handling gaps in visibility and camera handovers.
4.  **Event Logic:** A **Zone Manager** detects interactions with user-defined polygons (Entry/Exit/Intrusion).
5.  **Metadata Storage:** All tracking and event data are stored in **SQLite**, creating a permanent index of the footage.
6.  **Query & Retrieval:** A natural language **Query Engine** parses user intent and translates it into SQL filters, enabling instant retrieval of relevant video clips.

---

## 🛠 Tech Stack

-   **Language:** Python 3.10+
-   **Computer Vision:** OpenCV, Ultralytics (YOLOv8)
-   **Tracking:** DeepSORT / ByteTrack
-   **Database:** SQLite (Metadata-driven retrieval)
-   **LLM Integration:** OpenAI / LangChain (for natural language query parsing)
-   **Testing:** Unittest (covering ReID logic and database integrity)

---

## 🚀 Key Components

### 1. Global Identity Manager (The Core)
The system solves the "ID Fragmentation" problem using a two-stage matching strategy:
-   **Stage 1 (Strong Match):** Uses high-confidence cosine similarity of ReID embeddings.
-   **Stage 2 (Soft Match):** Combines ReID similarity, shirt color matching (histogram-based), and temporal constraints to re-identify individuals after they leave and re-enter camera views.

### 2. Metadata-Driven Playback Engine
Unlike traditional systems that require re-running trackers to show results, our engine uses stored metadata to:
-   Instantly jump to the exact timestamp of an event.
-   Draw bounding boxes on-the-fly using cached coordinates.
-   Provide "Event Buffer" playback (showing 2s before and after an event for full context).

### 3. Polygon Zone Logic
Users can define custom zones of any shape. The system uses a point-in-polygon algorithm to detect precise boundary crossings, reducing false alarms from movement in non-critical areas.

---

## 🏁 Validation
The core identity matching logic has been rigorously tested using a custom test suite (`test_reid.py`), ensuring that the system correctly handles:
-   Camera handovers.
-   Identity expiration (time-based windows).
-   Visual appearance changes (color-assisted matching).
