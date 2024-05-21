# Natural Language to SQL Query App

This project is an end-to-end application that converts natural language input into SQL queries and executes those queries on a database, returning the results.

## Project Flow

1. **Prompt**: User inputs a natural language query.
2. **LLM**: The query is processed by a Language Model.
3. **GeminiPro**: The processed query is transformed into an SQL query.
4. **Query**: The SQL query is executed against the database.
5. **SQL Database**: The database processes the query and returns the results.
6. **Response**: The results are sent back to the user.

## Implementation

### Database Setup

1. **SQLite**: Use SQLite to create and manage the database.
2. **Insert Records**: Populate the database with sample records using Python.

### Application Structure

- **LLM Application**: Integrate the application with GeminiPro for natural language processing and SQL conversion.
- **SQL Database**: Execute the converted SQL queries against the database.

### Files and Directories

- `requirements.txt`: Lists all the libraries required for the project.
- `.env`: Contains the API key for accessing GeminiPro.
- `sql.py`: Responsible for creating the database and tables using Python.
- `app.py`: The main application file that handles the entire flow from natural language input to database query and response.

## Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/abhishek-kumawat-1/Text-to-SQL-App.git
    cd Text-to-SQL-App
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**
    - Create a `.env` file in the root directory.
    - Add your GOOGLE API key to the `.env` file.
      ```plaintext
      GOOGLE_API_KEY=your_api_key_here
      ```

4. **Create the Database**
    - Run `sql.py` to create the database and insert initial records.
      ```bash
      python sql.py
      ```

5. **Run the Application**
    - Start the application by running `app.py`.
      ```bash
      python app.py
      ```

## Usage

- Launch the application.
- Input your natural language query.
- The application processes the query and returns the corresponding results from the database.

## File Descriptions

- **`requirements.txt`**: Contains all the necessary libraries for the project.
- **`.env`**: Stores environment variables, including API keys.
- **`sql.py`**: Script to create the SQLite database and tables.
- **`app.py`**: Main application script to handle the entire process from natural language input to SQL query execution.


## Contact

For any inquiries or support, please contact `abhishek.kumawat.iitd@gmail.com`.

---

Thank you for using the Natural Language to SQL Query App!
