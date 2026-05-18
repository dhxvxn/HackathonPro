# 🎥 Demo Video Script (2 Minutes)

## 0:00 - 0:15 | The Problem
"CCTV surveillance is a bottleneck. Security teams spend hours manually scrubbing through footage to find a single person or event. Today, we're introducing Smart CCTV AI, a system that makes video footage as searchable as a web page."

## 0:15 - 0:45 | Core Tech (Surveillance Mode)
"Our system runs a high-speed pipeline using YOLOv8 for detection and DeepSORT for tracking. But what makes us different is our Metadata Index. We don't just watch; we log every movement, appearance, and zone interaction into a searchable SQL database in real-time."
*(Action: Show the multi-view camera feed with bounding boxes and IDs flashing)*

## 0:45 - 1:15 | Multi-Camera ReID (The Innovation)
"Identity management is hard across multiple cameras. Our custom Two-Stage ReID engine uses deep learning embeddings and shirt-color analysis to maintain a 'Global ID'. Even if someone leaves Camera 1 and enters Camera 2 minutes later, the system remembers them."
*(Action: Show a person walking between camera views and maintaining the same Global ID)*

## 1:15 - 1:45 | Natural Language Search
"Now, the search. Instead of a timeline, we use an AI-powered search console. I can ask: 'Find a person in the parking zone.' The system parses the intent, filters the metadata, and instantly retrieves the relevant clips."
*(Action: Type a query and show the results list)*

## 1:45 - 2:00 | Instant Playback & Context
"When I select a result, we get metadata-driven playback. We don't just show the clip; we highlight the exact object using its historical track data. It’s fast, precise, and intelligence-first. That’s Smart CCTV AI."
*(Action: Play a clip with the highlighted object)*
