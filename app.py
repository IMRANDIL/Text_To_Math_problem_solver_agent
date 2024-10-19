# import streamlit as st
# from sympy import symbols, Eq, solve
# from langchain_groq import ChatGroq
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_community.utilities import WikipediaAPIWrapper
# from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
# import re

# # Set up the streamlit app
# st.set_page_config(page_title="Text To Math Problem Solver And Data Search Assistant", page_icon="🧮")
# st.title("Text To Math Problem Solver And Data Search Assistant")

# groq_api_key = st.text_input(label="Groq API Key", type='password')

# if not groq_api_key:
#     st.info("Please add your Groq API Key to continue")
#     st.stop()

# llm = ChatGroq(api_key=groq_api_key, model="Gemma2-9b-It", streaming=True)

# # Initializing the tools
# wikipedia_wrapper = WikipediaAPIWrapper()

# wikipedia_tool = Tool(
#     name='Wikipedia',
#     func=wikipedia_wrapper.run,
#     description="A tool for searching the Internet to find information on the topics mentioned"
# )

# # Define a function to check if the input is an arithmetic operation
# def is_arithmetic(expression):
#     # Check if the input contains only numbers and arithmetic operators
#     return re.match(r"^[0-9\s\+\-\*\/\(\)]+$", expression)

# # Define a new function for solving algebraic equations using SymPy
# def solve_algebraic_expression(equation):
#     try:
#         # First try splitting by `==`, if it doesn't work, fall back to `=`
#         if '==' in equation:
#             lhs, rhs = equation.split('==')
#         elif '=' in equation:
#             lhs, rhs = equation.split('=')
#         else:
#             raise ValueError("The equation must contain an equality sign ('=' or '==').")

#         # Get the variable from the equation
#         var = symbols('x')
#         # Create an equation to solve
#         equation = Eq(eval(lhs.strip()), eval(rhs.strip()))
#         result = solve(equation, var)
#         return result
    
#     except Exception as e:
#         return str(e)

# # Define the function that handles both arithmetic and algebraic queries
# def solve_expression(expression):
#     try:
#         if is_arithmetic(expression):
#             # For arithmetic operations, directly evaluate the expression
#             result = eval(expression)
#             return result
#         else:
#             # For algebraic equations, solve using sympy
#             return solve_algebraic_expression(expression)
#     except Exception as e:
#         return str(e)

# calculator = Tool(
#     name="Calculator",
#     func=lambda equation: solve_expression(equation),
#     description="A tool for solving algebraic equations like '2x + 5 = 11' or simple arithmetic like '23 * 23'."
# )

# prompt = """
# You are an agent tasked with solving users' mathematical questions. Logically arrive at the solution and provide detailed explanations. Display the solution step by step for the question below:
# Question: {question}
# Answer:
# """

# prompt_template = PromptTemplate(
#     input_variables=['question'],
#     template=prompt
# )

# # Combine tools into chain
# chain = LLMChain(llm=llm, prompt=prompt_template)


# reasoning_tool = Tool(
#     name="Reasoning tool",
#     func=chain.run,
#     description="A tool for answering logic-based and reasoning questions."
# )

# # Initialize the agent
# assistant_agent = initialize_agent(
#     tools=[wikipedia_tool, calculator, reasoning_tool],
#     llm=llm,
#     agent="zero-shot-react-description",
#     verbose=False,
#     handle_parsing_error=True
# )

# if "messages" not in st.session_state:
#     st.session_state['messages'] = [
#         {"role": "assistant", "content": "Hi, I am Mathru Haiden who can answer all your math questions."}
#     ]

# for msg in st.session_state['messages']:
#     st.chat_message(msg['role']).write(msg['content'])

# # Function to generate the response
# def generate_response(question):
#     response = assistant_agent.invoke({'input': question})
#     return response

# # Start the interaction
# question = st.text_area("Enter your question:", "What is the value of x in the equation 2x + 5 = 11?")

# if st.button("Find my answer"):
#     if question:
#         with st.spinner("Generating..."):
#             st.session_state.messages.append({"role": "user", "content": question})
#             st.chat_message("user").write(question)
#             st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
#             response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
#             st.session_state.messages.append({"role": "assistant", "content": response})
#             st.success(response)


# import streamlit as st
# from sympy import symbols, Eq, solve
# from langchain_groq import ChatGroq
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_community.utilities import WikipediaAPIWrapper
# from langchain.agents import Tool, initialize_agent
# from langchain.callbacks import StreamlitCallbackHandler
# import re

# # Set up the streamlit app
# st.set_page_config(page_title="Text To Math Problem Solver And Data Search Assistant", page_icon="🧮")
# st.title("Text To Math Problem Solver And Data Search Assistant")

# groq_api_key = st.text_input(label="Groq API Key", type='password')

# if not groq_api_key:
#     st.info("Please add your Groq API Key to continue")
#     st.stop()

# llm = ChatGroq(api_key=groq_api_key, model="Gemma2-9b-It", streaming=True)

# # Initializing the tools
# wikipedia_wrapper = WikipediaAPIWrapper()

# wikipedia_tool = Tool(
#     name='Wikipedia',
#     func=wikipedia_wrapper.run,
#     description="A tool for searching the Internet to find information on the topics mentioned"
# )

# # Define a function to check if the input is an arithmetic operation
# def is_arithmetic(expression):
#     # Check if the input contains only numbers and arithmetic operators
#     return re.match(r"^[0-9\s\+\-\*\/\(\)]+$", expression)

# # Define a new function for solving algebraic equations using SymPy
# def solve_algebraic_expression(equation):
#     try:
#         if '==' in equation:
#             lhs, rhs = equation.split('==')
#         elif '=' in equation:
#             lhs, rhs = equation.split('=')
#         else:
#             raise ValueError("The equation must contain an equality sign ('=' or '==').")

#         var = symbols('x')
#         equation = Eq(eval(lhs.strip()), eval(rhs.strip()))
#         result = solve(equation, var)
#         return result
    
#     except Exception as e:
#         return str(e)

# # Define the function that handles both arithmetic and algebraic queries
# def solve_expression(expression):
#     try:
#         if is_arithmetic(expression):
#             result = eval(expression)
#             return result
#         else:
#             return solve_algebraic_expression(expression)
#     except Exception as e:
#         return str(e)

# calculator = Tool(
#     name="Calculator",
#     func=lambda equation: solve_expression(equation),
#     description="A tool for solving algebraic equations like '2x + 5 = 11' or simple arithmetic like '23 * 23'."
# )

# prompt = """
# You are an agent tasked with solving users' mathematical questions. Logically arrive at the solution and provide detailed explanations. Display the solution step by step for the question below:
# Question: {question}
# Answer:
# """

# prompt_template = PromptTemplate(
#     input_variables=['question'],
#     template=prompt
# )

# # Combine tools into chain
# chain = LLMChain(llm=llm, prompt=prompt_template)

# reasoning_tool = Tool(
#     name="Reasoning tool",
#     func=chain.run,
#     description="A tool for answering logic-based and reasoning questions."
# )

# # Initialize the agent
# assistant_agent = initialize_agent(
#     tools=[wikipedia_tool, calculator, reasoning_tool],
#     llm=llm,
#     agent="zero-shot-react-description",
#     verbose=False,
#     handle_parsing_error=True
# )

# if "messages" not in st.session_state:
#     st.session_state['messages'] = [
#         {"role": "assistant", "content": "Hi, I am Mathru Haiden who can answer all your math questions."}
#     ]

# for msg in st.session_state['messages']:
#     st.chat_message(msg['role']).write(msg['content'])

# # Function to generate the response
# def generate_response(question):
#     response = assistant_agent.invoke({'input': question})
#     return response

# # Start the interaction
# question = st.text_area("Enter your question:", "What is the value of x in the equation 2x + 5 = 11?")

# if st.button("Find my answer"):
#     if question:
#         with st.spinner("Generating..."):
#             st.session_state.messages.append({"role": "user", "content": question})
#             st.chat_message("user").write(question)

#             # Directly run the agent without additional callbacks
#             response = assistant_agent.run({'input': question})

#             st.session_state.messages.append({"role": "assistant", "content": response})
#             st.success(response)



import streamlit as st
from sympy import symbols, Eq, solve
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
import re

# Set up the streamlit app
st.set_page_config(page_title="Text To Math Problem Solver And Data Search Assistant", page_icon="🧮")
st.title("Text To Math Problem Solver And Data Search Assistant")

groq_api_key = st.text_input(label="Groq API Key", type='password')

if not groq_api_key:
    st.info("Please add your Groq API Key to continue")
    st.stop()

llm = ChatGroq(api_key=groq_api_key, model="Gemma2-9b-It", streaming=True)

# Initializing the tools
wikipedia_wrapper = WikipediaAPIWrapper()

wikipedia_tool = Tool(
    name='Wikipedia',
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find information on the topics mentioned"
)

# Define a function to check if the input is an arithmetic operation
def is_arithmetic(expression):
    # Check if the input contains only numbers and arithmetic operators
    return re.match(r"^[0-9\s\+\-\*\/\(\)]+$", expression)

# Define a new function for solving algebraic equations using SymPy
def solve_algebraic_expression(equation):
    try:
        if '==' in equation:
            lhs, rhs = equation.split('==')
        elif '=' in equation:
            lhs, rhs = equation.split('=')
        else:
            raise ValueError("The equation must contain an equality sign ('=' or '==').")

        var = symbols('x')
        equation = Eq(eval(lhs.strip()), eval(rhs.strip()))
        result = solve(equation, var)
        return result
    
    except Exception as e:
        return str(e)

# Define the function that handles both arithmetic and algebraic queries
def solve_expression(expression):
    try:
        if is_arithmetic(expression):
            result = eval(expression)
            return result
        else:
            return solve_algebraic_expression(expression)
    except Exception as e:
        return str(e)

calculator = Tool(
    name="Calculator",
    func=lambda equation: solve_expression(equation),
    description="A tool for solving algebraic equations like '2x + 5 = 11' or simple arithmetic like '23 * 23'."
)

# Updated prompt to ask for explanation and reasoning
prompt = """
You are an intelligent agent designed to solve mathematical and logic-based questions. Your goal is to solve the question logically and **explain your steps clearly**. 
For every answer, follow this structure:
1. **Identify the pattern or rule** being used.
2. **Apply the rule step-by-step** to reach the answer.
3. **Provide the answer** clearly at the end.

Question: {question}

Explanation with Answer:
"""

prompt_template = PromptTemplate(
    input_variables=['question'],
    template=prompt
)

# Combine tools into chain
chain = LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

# Initialize the agent
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=False,
    handle_parsing_error=True
)

if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {"role": "assistant", "content": "Hi, I am Mathru Haiden who can answer all your math questions."}
    ]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

# Function to generate the response
def generate_response(question):
    response = assistant_agent.invoke({'input': question})
    return response

# Start the interaction
question = st.text_area("Enter your question:", "What is the value of x in the equation 2x + 5 = 11?")

if st.button("Find my answer"):
    if question:
        with st.spinner("Generating..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            # Directly run the agent without additional callbacks
            response = assistant_agent.run({'input': question}, callbacks=[st_cb])

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.success(response)
