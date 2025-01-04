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


### Key Components
1. **Website Analysis**
   - Scrapes website content using Firecrawl API
   - Extracts relevant information for context
   - Provides metadata for agent understanding

2. **Conversation Management**
   - Maintains conversation history
   - Handles agent transfers
   - Manages session state
   - Processes function calls

3. **Research Capabilities**
   - Web search functionality
   - Data aggregation
   - Information synthesis

## Setup and Configuration

### API Keys Required
- FIRECRAWL_API_KEY
- OPENAI_API_KEY
- TAVILY_API_KEY

### Configuration Files
1. `.streamlit/secrets.toml`
   - Stores API keys securely
   - Should be added to .gitignore

2. `.gitignore`
   - Excludes sensitive files
   - Prevents API key exposure

## Usage Instructions

1. **Initial Setup**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   - Create `.streamlit/secrets.toml`
   - Add required API keys

3. **Run Application**
   ```bash
   streamlit run sales_agents.py
   ```

4. **Using the Application**
   - Enter target website URL
   - Wait for website analysis
   - Begin conversation with AI sales team
   - Use clear conversation button when needed

## Security Considerations
- API keys stored in secrets.toml
- Secrets file excluded from version control
- Secure communication with APIs
- Session state management

## Best Practices
1. Always provide valid website URLs
2. Allow time for website analysis
3. Be clear and specific in communications
4. Use the clear conversation feature between sessions
5. Monitor API usage and limits

## Limitations
- Requires valid API keys
- Website analysis depends on Firecrawl API access
- Response time may vary based on API performance
- Model limitations based on GPT-4 capabilities

## Future Enhancements
- Additional agent specializations
- Enhanced website analysis
- Improved conversation handling
- Extended research capabilities
- Analytics dashboard
- Multi-language support

## Support
For issues related to:
- API keys: Check respective API provider documentation
- Installation: Verify requirements.txt dependencies
- Runtime errors: Check API quotas and connectivity
- Application usage: Review usage instructions
