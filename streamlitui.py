# # import streamlit as st
# # from web import Chatbot
# # from bs4 import BeautifulSoup 
# # import requests 


# # url_list=[] 


# # def scrape(site):

# #     r = requests.get(site)

# #     s = BeautifulSoup(r.text, 'html.parser')

# #     for i in s.find_all('a'):
# #         if len(url_list) >= 50:
# #             return

# #         href = i.attrs['href']

# #         if href.startswith('/'):
# #                 site = site + href

# #                 if site not in urls:
# #                     url_list.append(site)

# #                     print(site)
               

# #                     scrape(site)



# # def main():
# #     st.title("Chatbot")

    
# #     url_input = st.text_input("Enter URL for data ingestion:")
# #     question_input = st.text_input("Ask a question:")

    
# #     if url_input:
# #         # scrape(url_input)
# #         # chatbot = Chatbot(urls=[url_input])
# #         chatbot = Chatbot(urls=url_list)


# #             with st.spinner("Ingesting data..."):
# #                 chatbot.ingest()
# #             st.success("Data ingested successfully!")


        
# #         with st.spinner("Initializing retrieval chain..."):
# #             chatbot.initialize_llm()
# #             chatbot.initialize_chain()
# #         st.success("Retrieval chain initialized successfully!")

       
# #         if question_input:
# #             with st.spinner("Thinking..."):
# #                 response = chatbot.ask_question(question_input)
# #             st.write("Response:", response)

# # if __name__ == "__main__":
# #     main()




import streamlit as st
from web import Chatbot
from bs4 import BeautifulSoup
import requests

def scrape(site, depth=2, max_urls=30):
    url_list = []
    if site not in url_list:
        url_list.append(site)

    def inner_scrape(current_site, current_depth):
        if current_depth == 0 or len(url_list) >= max_urls:
            return

        try:
            r = requests.get(current_site)
            s = BeautifulSoup(r.text, 'html.parser')

            for i in s.find_all('a'):
                if len(url_list) >= max_urls:
                    return

                href = i.get('href')
                if href and href.startswith('/'):
                    new_url = current_site.rstrip('/') + href
                    if new_url not in url_list:
                        print(new_url)
                        url_list.append(new_url)
                        inner_scrape(new_url, current_depth-1)
                elif href and href.startswith('http'):
                    if href not in url_list:
                        print(href)
                        url_list.append(href)
                        inner_scrape(href, current_depth-1)
        except Exception as e:
            print(f"Error scraping {current_site}: {e}")

    inner_scrape(site, depth)
    return url_list

def main():
    st.title("Chatbot")

    # Initialize session state variables
    if 'chatbot' not in st.session_state:
        st.session_state['chatbot'] = None
        st.session_state['urls'] = []

    url_input = st.text_input("Enter URL for data ingestion:")
    question_input = st.text_input("Ask a question:", key="question")

    # Ingest data if URL is provided and ingestion is not done yet
    if url_input and url_input not in st.session_state['urls']:
        
        url_list = scrape(url_input)
        

        if url_list:
            chatbot = Chatbot(urls=url_list)

            with st.spinner("Ingesting data..."):
                chatbot.ingest()
            st.success("Data ingested successfully!")

            with st.spinner("Initializing retrieval chain..."):
                chatbot.initialize_llm()
                chatbot.initialize_chain()
            st.success("Retrieval chain initialized successfully!")

            # Store the chatbot instance and URL in session state
            st.session_state['chatbot'] = chatbot
            st.session_state['urls'].append(url_input)
        else:
            st.error("No URLs found")

    # Display question input field and handle the question after ingestion
    if st.session_state['chatbot'] is not None:
        if question_input:
            with st.spinner("Thinking..."):
                response = st.session_state['chatbot'].ask_question(question_input)
            st.write("Response:", response)

if __name__ == "__main__":
    main()

