# Telegram Session Export API

This API provides an endpoint to export a Pyrogram session string for a Telegram bot. The exported session string can be used to restore a bot's session and maintain its state across multiple runs.

## Installation

1. Clone the repository:


2. Install the required dependencies:


## Usage

1. Start the API server:


2. Access the API root endpoint to check if the server is running:


3. Use the `/token` endpoint to export the Pyrogram session string:


Replace `<your_api_id>`, `<your_api_hash>`, and `<your_bot_token>` with your actual Telegram API credentials and bot token.

## API Endpoints

- `GET /`: Returns the status of the API server.

- `GET /token`: Exports the Pyrogram session string for the provided Telegram bot credentials.

  - Query Parameters:
    - `api_id`: The Telegram API ID.
    - `api_hash`: The Telegram API hash.
    - `bot_token`: The Telegram bot token.

  - Response:
    ```
    {
      "session": "<exported_session_string>"
    }
    ```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This API is built with [FastAPI](https://fastapi.tiangolo.com/) and [Pyrogram](https://docs.pyrogram.org/), which are excellent frameworks for building APIs and interacting with the Telegram API.

## Disclaimer

This API is provided as-is without any warranty. Use it at your own risk.
