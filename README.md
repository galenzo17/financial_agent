# Financial Agent

The Financial Agent is a sophisticated tool designed to leverage the power of OpenAI's GPT-4 model and the LangChain library, integrated with the Polygon.io API, to provide advanced insights into financial data. This solution is crafted with the aim of simplifying access to financial market data, news, and analytics through a conversational interface. Whether you're looking to get the last quote for a stock, financials of a company, aggregates, or the latest ticker news, the Financial Agent has got you covered.

## Features

- **Conversational Interface:** Utilizes GPT-4 to understand and process natural language queries.
- **Integrated Financial Tools:** Leverages the Polygon.io API for real-time financial data including quotes, news, financials, and aggregates.
- **Interactive Web Interface:** Provides a user-friendly Gradio interface for easy access and interaction.
- **Modular Design:** Built with LangChain and LangChain Community utilities, ensuring flexibility and scalability.

## Getting Started

To use the Financial Agent, you'll need to set up a few things first:

### Prerequisites

- Python 3.8 or later
- An API key from Polygon.io (for accessing financial data)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>

    Install the required Python packages:

    bash

pip install -r requirements.txt

Set your Polygon.io API key as an environment variable:

bash

    export POLYGON_API_KEY='your_api_key_here'

Running the Application

To launch the Financial Agent interface:

bash

python financial_agent.py

This command starts a local web server and opens the Gradio interface in your default web browser, where you can interact with the Financial Agent by entering your queries.
Architecture

The application is structured into three main sections:

    Tool Definitions: Setup of the tools and utilities required for accessing and processing financial data.
    Agent and Helper Functions: Definition of the agent logic and helper functions for executing tools based on the agent's decisions.
    LangGraph Workflow: Creation of a workflow graph that defines the sequence of actions and decision-making logic for processing user inputs through the agent.

Usage

Simply enter your financial query into the Gradio interface's text box and submit. The Financial Agent will process your query, interact with the necessary financial data tools, and return a detailed response directly in the interface.
