1. **Create a New Folder and Open with VS Code:**
   - Open Visual Studio Code.

2. **Clone the Repository:**
   - Open the terminal in VS Code.
   - Run the following command to clone the repository:
     ```sh
     https://github.com/rakesh-2132/LLM-ChatBot
     ```

3. **Navigate to the Repository Directory:**
   - Change to the cloned repository directory:
     ```sh
     cd LLM-ChatBot
     ```

4. **Install Required Libraries:**
   - You can run the previously listed commands to install the libraries, or create a `requirements.txt` file and install them with the following commands:
     ```sh
     pip freeze > requirements.txt
     pip install -r requirements.txt
     ```

5. **Set Up Environment Variables:**
   - Inside your local repository, create a `.env` file.
   - Add your OpenAI API key to the file:
     ```
     openai_api_key=your_api_key
     ```

6. **Run the Application:**
   - Start the Streamlit application by running:
     ```sh
     streamlit run streamlitui.py
     ```
   - Your chatbot will open in the local host.

7. **Start Data Ingestion and Ask Queries:**
   - Enter your URL and hit enter to start data ingestion.
   - You can then ask queries to the chatbot.
