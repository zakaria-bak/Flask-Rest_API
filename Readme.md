# Comprehensive REST API Development with Flask (Reposting v1: march 2, 2022)

## Description
This repository demonstrates the evolution of a RESTful API developed using Flask, showcasing three versions with increasing complexity:
1. In-Memory Storage
2. SQLite Database Integration
3. SQLAlchemy ORM Integration

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/zakaria-bak/python-WebScraping.git
   cd python-WebScraping ```

2. Create a new vitual environment

 ```sh
 python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate` 
 ```

3. Install dependencies:

 ```sh
pip install -r requirements.txt
 ```

## Running the API

### Version 1: In-Memory Storage

1. Navigate to the version1 directory:
 ```sh
cd version1
 ```

2. Run the API:

 ```sh
python main.py
 ```

### Version 2: SQLite Database Integration

1. Navigate to the version2 directory:
 ```sh
cd version2
 ```

2. Create the database tables:
 ```sh
python createtables.py
 ```

3. Run the API:
 ```sh
python main.py
 ```

### Version 3: SQLAlchemy ORM Integration

1. Navigate to the version3 directory:
 ```sh
cd version3
 ```

2. Run the API:
 ```sh
python main.py
 ```

## Testing the API
1. Use Postman to test the API endpoints.

# API Endpoints
## Version 1 Endpoints
- POST /auth - Authenticate and get a JWT token.
- GET /item/<name> - Get an item by name.
- DELETE /item/<name> - Delete an item by name.
- PUT /item/<name> - Update an item by name.
- GET /items - Get a list of all items.

## Version 2 & 3 Endpoints
- POST /auth - Authenticate and get a JWT token.
- POST /register - Register a new user.
- GET /item/<name> - Get an item by name.
- POST /item/<name> - Create a new item.
- DELETE /item/<name> - Delete an item by name.
- PUT /item/<name> - Update an item by name.
- GET /items - Get a list of all items.

# Contribution

Feel free to contribute by opening issues or submitting pull requests.















