# 🎥 Smart CCTV AI

An intelligent surveillance ecosystem that transforms traditional CCTV footage into a searchable, metadata-indexed database.

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](test_reid.py)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](requirements.txt)

## 🚀 Vision
Most CCTV footage is never watched. **Smart CCTV AI** makes video data actionable by using deep learning to track identities across cameras and enabling natural language search for security events.

---

## ✨ Key Features

-   **🔍 Natural Language Search:** Query your footage like a search engine—"person entering restricted zone".
-   **🎯 Multi-Camera ReID:** Consistent global identity tracking across different camera views.
-   **📍 Polygon Zone Manager:** Define complex areas of interest for precise intrusion detection.
-   **⚡ Metadata-Driven Playback:** Instant video retrieval and object highlighting using indexed coordinates.
-   **🧠 Multi-Model Pipeline:** Powered by YOLOv8, DeepSORT, and custom ReID feature extractors.

---

## 🛠 Tech Stack

-   **AI:** YOLOv8, DeepSORT, FastReID (fallback)
-   **Core:** Python, OpenCV, NumPy
-   **Storage:** SQLite (Metadata Index)
-   **LLM Interface:** LangChain (Search Intent Parsing)

---

## 📂 Project Structure

-   `app.py`: Main surveillance engine and multi-view processor.
-   `search_console.py`: Natural language query interface.
-   `reid.py`: Multi-camera identity matching logic.
-   `video_player.py`: Metadata-driven playback engine.
-   `docs/`: Detailed design and module documentation.

---

## 🚦 Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run Surveillance
```bash
python app.py
```

### 3. Search & Playback
```bash
python search_console.py
```

---

## 📄 Documentation
For a deep dive into the system architecture and implementation details, see:
-   [**Submission Overview**](SUBMISSION.md)
-   [**System Design**](docs/SYSTEM_DESIGN.md)
-   [**Demo Script**](DEMO_SCRIPT.md)

---

## 👨‍💻 Author
**Dhavan**  
CSE Student & AI Enthusiast

---
*Developed for the HYKR Build Hackathon 2026*
