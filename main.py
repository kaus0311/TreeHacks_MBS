import openai
import os
import tkinter as tk

# SETTING UP API KEY AND ENVIRONMENT
API_KEY = 'YOUR_KEY'
os.environ['OpenAI_Key'] = API_KEY
openai.api_key = os.environ['OpenAI_Key']

# DEFINING THE RESPONSE FUNCTION
def generate_response(prompt):
    response = openai.Completion.create(engine='text-davinci-002', prompt=prompt, max_tokens=500)
    return response['choices'][0]['text']

# DEFINING THE GUI INTERFACE
class MbsbotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MBS Healthbot")

        # Create the title label
        self.title_label = tk.Label(self.root, text="Your Personal AI Assistant")
        self.title_label.pack(pady=10)

        # Create the text label
        self.text_label = tk.Label(self.root, text="How can I assist you today?")
        self.text_label.pack(pady=10)

        # Create the text input box
        self.prompt_entry = tk.Entry(self.root, width=50)
        self.prompt_entry.pack(pady=10)

        # Create the response display area
        self.response_display = tk.Label(self.root, text="", wraplength=400)
        self.response_display.pack(pady=10)

        # CREATE BUTTON TO GENERATE RESPONSE
        self.generate_button = tk.Button(self.root, text="Get Assistance", command=self.generate_response)
        self.generate_button.pack(pady=10)

    def generate_response(self):
        prompt = self.prompt_entry.get()
        response = generate_response(prompt)
        self.response_display.configure(text=response)

# STARTING THE GUI
gui = MbsbotGUI()
gui.root.mainloop()




