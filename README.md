# AI Sales Team Assistant Documentation

## Overview
The AI Sales Team Assistant is a Streamlit-based web application that implements an intelligent sales team using multiple AI agents. The system analyzes website content and facilitates interactions with potential customers through specialized AI agents, each with distinct roles in the sales process.

## Features

### 1. Web Interface
- Clean, user-friendly Streamlit interface
- Website URL input for analysis
- Real-time chat interface
- Conversation history tracking
- Clear conversation functionality
- Informative sidebar with agent descriptions

### 2. AI Sales Team Agents

#### Sales Manager
- First point of contact
- Analyzes queries and delegates to appropriate team members
- Manages conversation flow
- Handles conversation endings
- Model: gpt-4o-mini

#### Lead Qualifier
- Implements BANT framework (Budget, Authority, Need, Timeline)
- Evaluates leads against Ideal Customer Profile (ICP)
- Scores leads (hot, warm, cold)
- Gathers comprehensive lead information
- Model: gpt-4o

#### Objection Handler
- Addresses customer concerns
- Uses empathy and active listening
- Provides solutions to objections
- Maintains professional communication
- Model: gpt-4o

#### Closer
- Implements C.L.O.S.E.R framework:
  - Clarify prospect's needs
  - Label problems clearly
  - Overview past attempts
  - Sell the vision
  - Explain solutions
  - Reinforce decisions
- Model: gpt-4o

#### Research Specialist
- Conducts web searches using Tavily API
- Analyzes market trends
- Provides data-driven insights
- Researches prospect companies
- Model: gpt-4o

### 3. API Integrations
- OpenAI API for AI agents
- Firecrawl API for website scraping
- Tavily API for web research

## Technical Architecture

### Dependencies 
streamlit
openai
tavily-python
requests
python-dotenv
git+https://github.com/openai/swarm.git
firecrawl-py