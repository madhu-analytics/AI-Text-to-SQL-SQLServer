# AI Text-to-SQL with SQL Server

An end-to-end AI-powered Text-to-SQL application built using Python, OpenAI, SQL Server, Docker, SQLAlchemy, Pandas, and Streamlit.

## Project Overview

This project allows users to interact with a SQL Server database using natural language instead of writing SQL manually.

For example, instead of writing a SQL query, a user can ask:

"Show me all orders."

The application retrieves the database schema, sends the schema and user's question to an OpenAI LLM, generates the SQL query, executes it against SQL Server, and returns the result.

## End-to-End Architecture

User → main.py → get_schema() → OpenAI LLM → Generated SQL → execute_query() → SQL Server → Pandas DataFrame → Result

## How the Application Works

1. The user enters a question in natural language.
2. `main.py` receives the question.
3. `get_schema()` retrieves the relevant database structure from SQL Server.
4. The schema and user question are provided to the OpenAI LLM.
5. The LLM generates the SQL query.
6. The generated SQL is passed to `execute_query()`.
7. SQLAlchemy connects to SQL Server.
8. SQL Server executes the query.
9. Pandas loads the query result into a DataFrame.
10. The result is returned to the user.

## Key Components

### main.py

Acts as the main orchestration layer.

Responsibilities include:

- Loading environment variables
- Creating the OpenAI client
- Retrieving database schema
- Accepting the user's question
- Building the LLM prompt
- Sending the question and schema to OpenAI
- Receiving the generated SQL
- Executing the SQL
- Returning the result

### mydb.py

Contains reusable database functions.

The main functions are:

- `get_schema()` — retrieves table and column metadata from SQL Server.
- `execute_query()` — executes the generated SQL and returns the result as a Pandas DataFrame.

## Database Schema Discovery

The application uses SQL Server's `INFORMATION_SCHEMA.COLUMNS` to retrieve metadata about the database.

The information includes:

- TABLE_SCHEMA
- TABLE_NAME
- COLUMN_NAME
- DATA_TYPE

This schema information is provided to the LLM so that it understands the available tables and columns before generating SQL.

An important concept learned from this project is that SQL Server already knows its own schema, but the LLM does not automatically know the structure of a private database. The application therefore retrieves the schema and provides it to the LLM.

## SQL Query Execution

Once the LLM generates the SQL query, the application sends it to SQL Server using the database layer.

The responsibility is separated:

- `get_schema()` → helps the LLM understand the database.
- OpenAI → generates SQL.
- `execute_query()` → sends SQL to SQL Server.
- SQL Server → executes the SQL.
- Pandas → handles the returned result.

## Database Environment

SQL Server is running inside Docker on the local machine.

The project uses:

- SQL Server
- Docker
- Azure Data Studio
- Database: `sqlcourse`
- Port: `1433`

Azure Data Studio was used to connect to and inspect the SQL Server database.

## Database Connection Architecture

Python → PyODBC → unixODBC → Microsoft ODBC Driver 18 → SQL Server → Docker

The project required configuring PyODBC, unixODBC, and Microsoft's ODBC Driver 18 to establish connectivity between Python and SQL Server.

## SQLAlchemy

SQLAlchemy is used as the database connection layer.

It provides a reusable database engine and works with Pandas for reading SQL query results.

This also helped avoid directly passing raw PyODBC connections to Pandas.

## Pandas

Pandas is used to load SQL query results into DataFrames.

This makes the returned database data easy to process and display in the Python application.

## OpenAI Integration

The OpenAI API is used for the Text-to-SQL step.

The LLM receives:

- Database schema
- User's natural-language question
- Instructions for generating SQL

The LLM then generates a SQL query that can be executed against the database.

The LLM generates the SQL; it does not directly execute the SQL against the database.

## Environment Variables

Sensitive information is stored in a local `.env` file.

The project uses `python-dotenv` and `os.getenv()` to load configuration values such as:

- OpenAI API key
- SQL Server host
- Database name
- SQL Server username
- SQL Server password

The actual `.env` file is intentionally excluded from GitHub.

## Git Security

The `.gitignore` file excludes sensitive and local development files such as:

- `.env`
- `myenv/`
- `__pycache__/`
- `*.pyc`
- `.idea/`
- `.DS_Store`

API keys and database passwords are therefore kept out of the GitHub repository.

## Streamlit

The project also contains Streamlit code for creating an interactive user interface.

The Streamlit application provides a more user-friendly way to interact with the Text-to-SQL workflow instead of using only the terminal.

## Technologies Used

- Python
- OpenAI API
- SQL Server
- Docker
- SQLAlchemy
- Pandas
- PyODBC
- unixODBC
- Microsoft ODBC Driver 18
- Streamlit
- python-dotenv
- PyCharm
- Azure Data Studio
- Git
- GitHub

## Project Structure

Day1_dataGPT/
- main.py — Main application and LLM orchestration
- mydb.py — Database connection, schema discovery, and query execution
- streamlit.py — Streamlit application
- streamlit_demo.py — Streamlit demonstration
- req.txt — Python dependencies
- Pipfile — Project environment/dependency configuration
- .gitignore — Files excluded from Git
- .env — Local environment variables, not committed to GitHub

## Key Concepts Learned

This project helped me understand how an LLM can be connected to a real database and used as part of an AI application.

Key concepts include:

- LLM API integration
- Text-to-SQL
- Prompt construction
- Database schema discovery
- SQL Server connectivity
- Docker
- PyODBC
- unixODBC
- Microsoft ODBC Driver 18
- SQLAlchemy
- Pandas
- Environment variables
- Streamlit
- Git and GitHub

The most important architecture I learned is:

Natural Language → LLM → SQL → Database → Result

The LLM understands the user's intent and generates SQL, while the Python application and SQL Server handle the actual execution.

## Setup

1. Clone the repository.
2. Create a Python virtual environment.
3. Activate the virtual environment.
4. Install the dependencies from `req.txt`.
5. Make sure the SQL Server Docker container is running.
6. Create a local `.env` file with the required OpenAI and SQL Server credentials.
7. Run `main.py` to use the Python application.
8. Run the Streamlit application to use the browser-based interface.

## Troubleshooting Lessons

During development, several issues were encountered and resolved, including:

- PyODBC library loading issues on macOS
- Installing and configuring unixODBC
- Installing Microsoft ODBC Driver 18
- SQLAlchemy connection URL issues
- Pandas connection warnings
- SQL Server database selection
- SQL Server schema/table references
- Environment variable configuration

These issues helped build a better understanding of how Python, ODBC, SQLAlchemy, Docker, and SQL Server work together.

## Future Improvements

Possible improvements include:

- Add SQL query validation
- Restrict generated queries to read-only operations
- Improve prompt engineering
- Add better error handling
- Support multiple tables
- Add data visualizations
- Improve the Streamlit interface
- Add conversational history
- Add AI tool calling
- Connect additional external APIs
- Build an MCP server around the application's tools

## Project Status

Completed — Day 1 AI application project.

This project forms the foundation for the next stage of my AI engineering learning journey:

LLM → Tool Calling → External APIs → MCP → AI Agents
