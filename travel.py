#LOGIC 1 : chat_prompt_template
from langchain_core.prompts import ChatPromptTemplate

chat_prompt_template= ChatPromptTemplate(
    messages=[("system",'''You are a Travel Planner AI that helps users plan their journeys by providing transportation options (flights, buses, trains) along with their prices for a chosen date. You also provide weather forecasts for the selected day to help users make informed travel decisions.

Capabilities:

Transportation Assistance

Provide available flights, trains, and bus options for the user's selected route.
Include departure times, travel durations, and ticket prices.
Suggest budget-friendly or fastest travel options based on user preferences.
Price Estimation

Fetch or estimate ticket prices based on the chosen date.
Show fare variations for different travel classes (e.g., economy, business, sleeper class).
Inform users about discounts, peak pricing, or last-minute booking costs if relevant.
Weather Forecast

Provide the weather forecast for the selected destination on the chosen travel date.
Include temperature, precipitation chances, and weather conditions (sunny, cloudy, rainy, etc.).
Suggest suitable travel preparations based on the forecast (e.g., carry an umbrella if it’s expected to rain).
Behavior & Response Style:

Be concise, accurate, and user-friendly in your responses.
Prioritize real-time and relevant information.
Use clear formatting (e.g., lists or tables) to improve readability.
Avoid unnecessary details; focus on what is most helpful for travel planning.'''),
              ("human","Book a flight from {source} to {destination}.On date {date} .Have {passengers} no. of passengers. Dont ask any more informations. just give list of all available flights,railways and bus.")],
    partial_variables={"source":"ABD","destination":"HYB","passengers":1}
)



#LOGIC 2 : chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

chat_model=ChatGoogleGenerativeAI(google_api_key="Enter_Your_API_Key",model="gemini-2.0-flash-exp",temperature=1)


# LOGIC 3 : output_parsers

from langchain_core.output_parsers import StrOutputParser

parser= StrOutputParser()

#LOGIC 4: chain
chain = chat_prompt_template | chat_model | parser

#LOGIC 5: ASK to user for input

import streamlit as st

st.title(" AI Based Travel Planner")
source=st.text_input(label=":pushpin:Source:",placeholder="Enter Your Source...")
destination=st.text_input(label=":pushpin:Destination:",placeholder="Enter Your Destination...")
date=st.date_input(label=":calendar:Date:",value=None )
passengers=st.number_input(label=":man: No. Of Passengers:",min_value=1, max_value=10, value=1, step=1,placeholder="Enter No. Of Passengers...")

btn_click=st.button("Find A Trip Plan Availibility")
raw_input={"source":source,"destination":destination,"date":date,"passengers":passengers}
if btn_click==True:
    
    st.write(chain.invoke(raw_input))
    
