# Import the necessary libraries
import tkinter as tk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset into a DataFrame
df = pd.read_csv("df_queries.csv")
# print(df.shape)
# 2574248,4
# dataset is quite big, with more than 2.5 mil entries


# Preprocess the input text
def preprocess(text):
    text = text.lower()
    text = "".join(c for c in text if c.isalnum() or c.isspace())
    words = text.split()
    return " ".join(words)


# Vectorize the dataset using TF-IDF
vectorizer = TfidfVectorizer()
corpus = df["query"].apply(preprocess)
X = vectorizer.fit_transform(corpus)


# Define a function to get the top 10 most similar queries
def get_top_queries(text):
    # Preprocess the input text
    text = preprocess(text)

    # Vectorize the input text
    vec = vectorizer.transform([text])

    # Calculate the cosine similarity between the input text and each query in the dataset
    sim_scores = cosine_similarity(vec, X)

    # Get the indices and relevance scores of the top 10 most similar queries
    top_indices = sim_scores.argsort()[0][-10:][::-1]
    top_scores = sim_scores[0][top_indices]

    # Get the top 10 most similar queries and their relevant columns and scores
    top_queries = df.iloc[top_indices].reset_index(drop=True)
    top_queries["relevance"] = top_scores

    # Return the top 10 most similar queries
    return top_queries[
        ["relevance", "query", "searches_per_month", "success_rate", "conversion_rate"]
    ]


class QueryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("Search Engine")

        # Create the input label and text box
        input_label = tk.Label(self, text="Enter some text:")
        input_label.pack()
        self.input_text = tk.Entry(self)
        self.input_text.pack()

        # Create the "Search Query" button
        search_button = tk.Button(self, text="Search Query", command=self.greet)
        search_button.pack()

        # Create a frame below the button for the pandas dataframe
        self.df_frame = tk.Frame(self)
        self.df_frame.pack(fill="both", expand=True)

        # Create an empty pandas dataframe table inside the frame
        data = {
            "Relevance": [],
            "Query": [],
            "Search_per_month": [],
            "Success Rate": [],
            "Conversion Rate": [],
        }
        self.df = pd.DataFrame(data)
        self.df_table = tk.Text(self.df_frame, font=("Courier", 12))
        self.df_table.insert("end", self.df.to_string(index=False))
        self.df_table.pack(fill="both", expand=True)

    def greet(self):
        # Get the input text
        text = self.input_text.get()

        # Generate the confirmation message
        confirmation_message = "I got your query"

        # Generate the greeting message with the input text
        query_message = f"{confirmation_message}: {text}"

        # Display the greeting message in the main window
        label = tk.Label(self, text=query_message, font=("Helvetica", 16))
        label.pack()

        # Update the pandas dataframe with new data
        # data = {"Relevance": ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Isabella", "Jack"],
        #         "Query": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]}
        self.df = get_top_queries(text)

        # Update the table with the new dataframe
        self.df_table.delete("1.0", "end")
        self.df_table.insert("end", self.df.to_string(index=False))
        # input_text = 'How to make pizza at home'
        # top_queries = get_top_queries(input_text)


if __name__ == "__main__":
    app = QueryApp()
    app.mainloop()
