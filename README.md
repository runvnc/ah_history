# AH History Plugin

A chat history viewer plugin for Assistant Hub that displays past conversations organized by date.

## Features

- Displays recent chat sessions in the sidebar
- Groups chat sessions by date
- Shows preview of each chat's first message
- Clickable links to full chat sessions
- Modern web component architecture using Lit

## Installation

The plugin is packaged as a Python package and can be installed using pip:

```bash
pip install -e .
```

## Structure

```
ah_history/
├── src/
│   └── ah_history/
│       ├── static/
│       │   └── js/
│       │       ├── base.js
│       │       ├── chat-history.js
│       │       └── lit-core.min.js
│       ├── inject/
│       │   └── history.jinja2
│       └── mod.py
├── plugin_info.json
├── pyproject.toml
└── setup.py
```

## Configuration

The plugin is configured through `plugin_info.json`:

- Provides a GET route for `/session_list/{agent}`
- Injects the history viewer component into the sidebar
- Uses Lit-based web components for the UI

## Development

To modify the plugin:

1. Frontend components are in `static/js/`
2. Backend routes are in `mod.py`
3. Template injection is configured in `inject/history.jinja2`

## API

### GET /session_list/{agent}

Returns recent chat sessions for the specified agent.

Response format:
```json
[
  {
    "log_id": "unique_chat_id",
    "descr": "First 80 characters of the chat...",
    "date": 1234567890
  }
]
```
