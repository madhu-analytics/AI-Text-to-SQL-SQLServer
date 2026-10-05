# AI Text-to-SQL with SQL Server

A Python-based Text-to-SQL application that uses an OpenAI LLM to convert natural-language questions into SQL queries and execute those queries against a SQL Server database running in Docker.

## Project Overview

The goal of this project is to allow users to interact with a SQL Server database using natural language instead of writing SQL manually.

For example:

User:

> Show me all orders.

The application retrieves the database schema, provides the schema and the user's question to the LLM, receives the generated SQL query, executes it against SQL Server, and returns the result.

## Architecture

```text
User
  |
  v
main.py
  |
  v
get_schema()
  |
  v
OpenAI LLM
  |
  | Generates SQL
  v
execute_query()
  |
  v
SQL Server
  |
  v
Pandas DataFrame
  |
  v
Result
