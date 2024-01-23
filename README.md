# Real-Time Chat Application

## Overview

This is a real-time chat application built with React for the front end and Django with Channels for the backend. The communication is facilitated over the RTP (Real-Time Protocol) using WebSockets.

## Features

- **Real-Time Communication:** Utilizes WebSockets to enable instant messaging and real-time updates.
- **React Front End:** The user interface is built using React, providing a responsive and dynamic user experience.
- **Django with Channels:** Backend server implemented with Django, utilizing Django Channels for WebSocket support.

## Prerequisites

Make sure you have the following installed before running the application:

- Node.js and npm for the React front end.
- Python and Django for the backend.

## Installation

### Front End (React)

1. Navigate to the `frontend` directory.
2. Install dependencies: `npm install`.
3. Start the development server: `npm start`.

### Back End (Django with Channels)

1. Navigate to the `backend` directory.
2. Install Django and required packages: `pip install -r requirements.txt`.
3. Apply migrations: `python manage.py migrate`.
4. Run the development server: `python manage.py runserver`.

## Usage

1. Access the application in your browser at [http://localhost:3000](http://localhost:3000).
2. Start chatting in real-time with other users.

## Contributing

We welcome contributions! If you'd like to contribute, please follow the steps outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE).
