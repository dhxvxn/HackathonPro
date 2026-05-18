# Project Structure (Flat Layout)

smart-cctv-ai/
├── app.py              # Main entry point (Streamlit/UI)
├── detector.py         # Object detection logic (YOLO)
├── tracker.py          # Object tracking (DeepSORT/ByteTrack)
├── reid.py             # Re-identification & Feature Extraction
├── event.py            # Event detection & logging logic
├── db.py               # Database connection & basic operations
├── db_schema.py        # Database schema definitions
├── query_engine.py     # SQL query generation & execution
├── intent_manager.py   # Natural language intent parsing
├── llm_parser.py       # LLM integration for query parsing
├── zone_manager.py     # Management of detection zones
├── zone_logic.py       # Geometric logic for zones
├── video_player.py     # Video playback & clip extraction
├── heatmap.py          # Heatmap generation logic
├── search_console.py   # CLI/Terminal search interface
├── zones.json          # Zone configuration storage
└── docs/               # System documentation