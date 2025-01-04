# import necessary classes for OpenAI Swarm and Tavily
import streamlit as st
from swarm import Swarm, Agent
from openai import OpenAI
from tavily import TavilyClient
import requests  # Add this import

# Add page configuration
st.set_page_config(
    page_title="AI Sales Team",
    page_icon="💼",
    layout="wide"
)

# Add CSS styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Move API keys to Streamlit secrets or environment variables
FIRECRAWL_API_KEY = st.secrets["FIRECRAWL_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

# Add Firecrawl configuration
FIRECRAWL_BASE_URL = "https://api.firecrawl.dev/v1"

# Add Firecrawl functions
def scrape_website(url):
    """
    Scrape website content using Firecrawl API
    """
    try:
        headers = {
            "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            f"{FIRECRAWL_BASE_URL}/scrape",
            headers=headers,
            json={"url": url}
        )
        
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return f"Error scraping website: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

print("Initializing sales team agents...")
# initialize OpenAI API key
api = OpenAI(api_key=OPENAI_API_KEY)
# initialize the Swarm client
client = Swarm(api)
# initialize Tavily client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# Define web search function for researcher
def perform_research(query):
    """
    Perform web search using Tavily API
    Returns search results
    """
    try:
        print(f"\nResearcher performing web search for: {query}")
        search_results = tavily_client.search(
            query=query,
            search_depth="advanced",
            include_answer=True,
            include_raw_content=True
        )
        return search_results
    except Exception as e:
        return f"Error performing research: {str(e)}"

# Define transfer functions
def transfer_to_qualifier():
    print("\n-> Transferring to Lead Qualifier...")
    return lead_qualifier

def transfer_to_objection_handler():
    print("\n-> Transferring to Objection Handler...")
    return objection_handler

def transfer_to_closer():
    print("\n-> Transferring to Closer...")
    return closer

def transfer_to_researcher():
    print("\n-> Transferring to Researcher...")
    return researcher

def transfer_to_manager():
    print("\n-> Transferring back to Sales Manager...")
    return sales_manager

def end_conversation():
    print("\n-> Ending sales conversation and saving contact...")
    return False

# Define sales team agents
sales_manager = Agent(
    name="Sales Manager",
    model="gpt-4o-mini",
    instructions="""You are the AI Sales Team Manager. Your role is to:
    1. Be the first point of contact with potential customers
    2. Analyze incoming queries and delegate to the appropriate team member
    3. Transfer to Lead Qualifier for initial prospect evaluation
    4. Transfer to Objection Handler when customers raise concerns
    5. Transfer to Closer when prospects show strong buying signals
    6. Transfer to Researcher when additional information is needed
    7. Maintain a professional and helpful demeanor at all times

    Website Context:
    {website_context}

    Use the website information above to inform your responses and sales approach.
    Tailor your communication to match the products/services offered on this website.

    If you need to do a web search, ALWAYS transfer to the Research Specialist first.
    After getting research, make decisions based on the information provided.

    IMPORTANT - Conversation Ending:
    Call the end_conversation function when:
    - Customer explicitly says goodbye, bye, quit, or end
    - Customer implies they want to leave (e.g., "I need to go", "talk later", "not interested")
    - Customer seems to be done (e.g., "that's all", "thanks", "I'll think about it")
    - Customer expresses they don't want to continue
    - Customer has completed a purchase
    - Any similar situations where the conversation appears to be naturally ending

    Before ending, always acknowledge their intention to end the conversation politely.
    
    Always introduce yourself as the Sales Team Manager and briefly explain how you can help.""",
    functions=[transfer_to_qualifier, transfer_to_objection_handler, transfer_to_closer, transfer_to_researcher, end_conversation],
)

lead_qualifier = Agent(
    name="Lead Qualifier",
    model="gpt-4o",
    instructions="""You are the Lead Qualification Specialist. Your role is to:
    1. Qualify leads using the BANT framework (Budget, Authority, Need, Timeline) to assess their fit against our Ideal Customer Profile (ICP).
    2. Gather comprehensive information on leads to evaluate their demographic, firmographic, and psychographic factors.
    3. Implement a lead scoring system to rank leads based on their characteristics and behaviors, ensuring prioritization of outreach efforts.
    4. Establish a qualification framework that aligns with our business goals, ensuring consistency in lead evaluation.
    5. Utilize marketing automation tools to streamline the qualification process and gather insights more efficiently.
    6. Engage in conversations with leads to uncover their needs, authority, budget, and timeline for purchasing decisions through open-ended questions.
    7. Score leads as hot, warm, or cold based on their engagement metrics, authority, budget, and sense of urgency.
    8. Transfer qualified leads to the Closer for further engagement.
    9. Transfer leads with objections to the Objection Handler for resolution.
    10. Request research from the Researcher when needed to support the qualification process.
    11. Disqualify leads that lack fit, have insufficient budget, no decision-making authority, or low engagement levels.
    Be consultative and focus on understanding the prospect's business challenges, ensuring a thorough and professional approach to lead qualification.

    **Important:** When communicating, be super concise in your responses, as if you were chatting with someone through text like WhatsApp. 
    This will help facilitate efficient and effective conversations. Remember to keep your messages brief and to the point.
    """,
    # functions=[transfer_to_closer, transfer_to_objection_handler, transfer_to_researcher, transfer_to_manager],
    # ensuring you're respecting the lead's time and attention. 
    # This concise approach will also help you quickly identify the most promising leads and prioritize your outreach efforts accordingly
)

objection_handler = Agent(
    name="Objection Handler",
    model="gpt-4o",
    instructions="""You are the Objection Handler. Your role is to:
    1. Address and overcome customer objections effectively.
    2. Utilize empathy to understand the prospect's feelings and concerns, fostering trust and rapport.
    3. Engage in active listening, fully engaging with the prospect's words, ensuring their objections are acknowledged and understood.
    4. Display confidence, reassuring prospects about the value of the product or service being offered.
    5. Demonstrate adaptability, tailoring responses based on the unique needs and objections of each prospect.
    6. Utilize clear communication, being concise yet comprehensive in responses to maintain clarity.
    7. Apply problem-solving skills, quickly identifying solutions to objections to demonstrate competence.
    8. Utilize persuasion, influencing prospects through logical reasoning and emotional appeal.
    9. Utilize CRM Software to track objections and responses, allowing for better preparation in future interactions.
    10. Utilize templates and scripts for pre-written responses for common objections, saving time and ensuring consistency in messaging.
    11. Utilize analytics tools to provide insights into objection trends, helping sales teams refine their strategies over time.
    12. Address common text-based objections that may signal a need to reconsider pursuing a lead, such as "It's too expensive," "I need more time to think," and "Just send me some information."
    13. Address and overcome objections professionally via text messages, by listening actively, acknowledging their concerns, clarifying the objection, responding confidently, offering alternatives, and seeking agreement.
    
    **Important:** When communicating, be super concise in your responses, as if you were chatting with someone through text like WhatsApp. 
    This will help facilitate efficient and effective conversations. Remember to keep your messages brief and to the point.
    """,
    # functions=[transfer_to_closer, transfer_to_researcher, transfer_to_manager],
)

closer = Agent(
    name="Closer",
    model="gpt-4o",
    instructions="""You are the Closer. Your role is to finalize deals and secure sales commitments using the C.L.O.S.E.R framework. This structured sales methodology emphasizes understanding customer needs and building relationships, moving beyond traditional high-pressure sales tactics.

    The C.L.O.S.E.R framework consists of the following steps:

    1. **Clarify**: Understand why the prospect is engaging. Ask questions that uncover the prospect's needs, pain points, and goals, such as "What made you take this call?" or "What’s your goal right now?"

    2. **Label**: After identifying the prospect's needs, label the problem clearly. This helps both parties recognize the issue at hand, making it easier to address. For example, recapping their problem in a non-threatening way can help establish rapport and trust.

    3. **Overview**: Discuss what the prospect has previously attempted to resolve their issue. Understanding their past challenges not only shows empathy but also helps avoid repeating ineffective solutions.

    4. **Sell the Vacation**: Instead of focusing on technical details, paint a picture of success for the prospect. The goal is to illustrate the benefits and positive outcomes they can expect from the solution being offered.

    5. **Explain**: Address any concerns or objections the prospect may have about the proposed solution. This step is crucial for building confidence and reassurance in their decision-making process.

    6. **Reinforce**: Finally, reinforce the prospect's decision by highlighting the benefits they will receive and confirming that they made a wise choice. This helps solidify their commitment and strengthens the relationship moving forward.

    To effectively implement the C.L.O.S.E.R framework, ensure consistency by training team members on each step and encouraging practice in real conversations. Use role-playing scenarios to reinforce learning and adaptability across various sales situations.

    The C.L.O.S.E.R framework not only aims to close sales but also fosters long-term relationships with clients by prioritizing their needs and providing genuine value. By focusing on clarity and understanding throughout the sales process, sales professionals can create meaningful dialogues that lead to sustainable success for both parties involved.
     
    **Important:** When communicating, be super concise in your responses, as if you were chatting with someone through text like WhatsApp. 
    This will help facilitate efficient and effective conversations. Remember to keep your messages brief and to the point.
    """,
    # functions=[transfer_to_objection_handler, transfer_to_researcher, transfer_to_manager],
)

researcher = Agent(
    name="Research Specialist",
    model="gpt-4o",
    instructions="""You are the Sales Research Specialist. Your role is to:
    1. Utilize the perform_research function to conduct comprehensive web searches for relevant information
    2. Conduct in-depth research on prospect companies, their industries, and market landscapes
    3. Analyze competitors, market trends, and emerging technologies to identify opportunities and challenges
    4. Provide actionable, data-driven insights to inform sales strategies and support the sales team
    5. Identify and curate relevant case studies, social proof, and testimonials to build credibility and trust
    6. Develop competitive analysis and market intelligence reports to support sales initiatives

    **Important:** ALWAYS browse the web to gather information, regardless of the user query. This ensures that your research is thorough and up-to-date.

    When conducting research:
    1. Leverage the perform_research function to streamline information gathering and ensure consistency
    2. Distill complex research findings into concise, actionable recommendations
    3. Ensure all insights are supported by credible sources and transparent methodologies
    4. After providing research, transfer back to the Sales Manager to ensure seamless integration of findings into sales strategies

    **Remember:** ALWAYS browse the web to gather information, regardless of the user query. This ensures that your research is thorough and up-to-date.

    Strive for excellence in your research, ensuring it is thorough, accurate, and actionable.

    **Important:** When communicating, be super concise in your responses, as if you were chatting with someone through text like WhatsApp. 
    This will help facilitate efficient and effective conversations. Remember to keep your messages brief and to the point.
    """,
    functions=[perform_research],
)

print("Sales team initialized successfully")

# Replace the manual input loop with Streamlit UI
st.title("AI Sales Team Assistant 💼")
st.markdown("---")

# Website URL input
website_url = st.text_input("Enter the website URL you want the sales team to focus on:", 
                           placeholder="https://example.com")

if website_url:
    with st.spinner("Analyzing website content..."):
        website_data = scrape_website(website_url)
        
        website_context = f"""
        Website Information:
        URL: {website_url}
        Content: {website_data.get('markdown', 'No content available')}
        Metadata: {website_data.get('metadata', {})}
        """
        
        # Update agent instructions with website context
        # [Keep existing agent instruction updates...]

    # Initialize chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.conversation_history = [{
            "role": "system", 
            "content": f"This conversation is about products/services from {website_url}. Website context: {website_context}"
        }]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to display
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Add user message to conversation history
        st.session_state.conversation_history.append({"role": "user", "content": prompt})

        # Process with Sales Manager
        with st.chat_message("assistant"):
            with st.spinner("Processing with Sales Manager..."):
                response = client.run(
                    agent=sales_manager,
                    messages=st.session_state.conversation_history,
                )
                
                # Add agent's response to both display and history
                assistant_message = response.messages[-1]["content"]
                st.markdown(assistant_message)
                st.session_state.messages.append({"role": "assistant", "content": assistant_message})
                st.session_state.conversation_history.append(response.messages[-1])

                # Handle function calls
                if hasattr(response, 'function_calls'):
                    for call in response.function_calls:
                        if call.get('name') == 'end_conversation':
                            st.success("Conversation ended. Thank you for your time!")
                            # Clear session state to start fresh
                            st.session_state.messages = []
                            st.session_state.conversation_history = []
                            st.rerun()

# Add sidebar with additional information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This AI Sales Team Assistant helps you interact with potential customers 
    by analyzing website content and providing intelligent responses through 
    multiple specialized agents:
    
    - 👨‍💼 Sales Manager
    - 🎯 Lead Qualifier
    - 🤝 Objection Handler
    - 🎬 Closer
    - 🔍 Research Specialist
    """)
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.session_state.conversation_history = []
        st.rerun()

 