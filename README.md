# Photo-Video-Sharing-App-FastAPI

A full-stack asynchronous media-sharing platform. This project demonstrates a production-ready backend architecture featuring secure JWT authentication, relational database mapping, and direct-to-cloud media processing.

## 🚀 Live Demo

- **Frontend UI:** https://picfeed.streamlit.app/
- **Backend API Docs:** https://photo-video-sharing-app-fastapi-production.up.railway.app/docs

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python 3.12, Uvicorn
- **Database:** SQLite (Async via `aiosqlite`), SQLAlchemy (ORM)
- **Frontend:** Streamlit
- **Authentication:** `fastapi-users` (JWT-based, Bearer transport)
- **Cloud Storage:** ImageKit v5 SDK
- **Deployment:** Railway (API) & Streamlit Community Cloud (UI)

## ✨ Core Engineering Features

- **Asynchronous Concurrency:** Non-blocking database transactions using `aiosqlite` to handle multiple simultaneous user requests.
- **Stateless Authentication:** Secure user registration and session management via JWTs.
- **Relational Mapping:** Strict database schemas enforcing foreign-key constraints (linking media posts to user UUIDs).
- **Cloud Media Pipeline:** Direct integration with ImageKit for secure file uploads, URL generation, and on-the-fly transformations (watermarking, resizing) to offload storage from the local server.

