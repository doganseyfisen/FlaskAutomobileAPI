# Flask Automobile API

This Flask application provides a simple API named "Automobiles." The data for automobiles is fetched from https://www.autotrader.co.uk/cars, and it allows users to view, add, update, and delete automobile records.

## Requirements

- Python 3.x
- Flask (and its dependencies)

## Installation

1. Navigate to the project directory.

2. Install Flask and other dependencies by running the following command:
   ```
   pip install flask flask_restful
   ```

## Usage

1. Start the Flask server by running the following command:
   ```
   python automobile.py
   ```

2. After the server starts, you can access it by visiting `http://localhost:5000/` in your web browser or using a cURL command in a terminal.

3. API Endpoints:

   - **GET** `/automobiles`: Lists all automobiles.
   - **POST** `/automobiles`: Adds a new automobile. Send the request in JSON format and include the following parameters:
      - `brand` (required): The automobile brand.
      - `model` (required): The automobile model.
      - `body` (required): The automobile body type.
      - `fuel` (required): The automobile fuel type.
      - `price` (required): The automobile price.
      - `seats` (required): The number of seats in the automobile.

   - **GET** `/automobiles/<automobile_id>`: Retrieves details of a specific automobile.
   - **PUT** `/automobiles/<automobile_id>`: Updates a specific automobile. Send the request in JSON format and include the following parameters:
      - `brand` (required): The automobile brand.
      - `model` (required): The automobile model.
      - `body` (required): The automobile body type.
      - `fuel` (required): The automobile fuel type.
      - `price` (required): The automobile price.
      - `seats` (required): The number of seats in the automobile.

   - **DELETE** `/automobiles/<automobile_id>`: Deletes a specific automobile.

4. Example Usage:

   - To list all automobiles:
     ```bash
     curl http://localhost:5000/automobiles
     ```

   - To add a new automobile (e.g., Ford Focus):
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"brand": "Ford", "model": "Focus", "body": "Estate", "fuel": "Diesel", "price": 24470, "seats": 5}' http://localhost:5000/automobiles
     ```

   - To retrieve details of a specific automobile (e.g., "automobile1"):
     ```bash
     curl http://localhost:5000/automobiles/automobile1
     ```

   - To update a specific automobile (e.g., "automobile2"):
     ```bash
     curl -X PUT -H "Content-Type: application/json" -d '{"brand": "Toyota", "model": "Camry", "body": "Sedan", "fuel": "Petrol", "price": 30000, "seats": 5}' http://localhost:5000/automobiles/automobile2
     ```

   - To delete a specific automobile (e.g., "automobile3"):
     ```bash
     curl -X DELETE http://localhost:5000/automobiles/automobile3
     ```

## Notes

- This application is created for demonstration purposes. In a real project, additional security measures and error handling should be implemented.
