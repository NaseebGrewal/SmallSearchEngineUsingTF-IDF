# SmallSearchEngineUsingTF-IDF

This repository contains a simple implementation of a search engine using the **TF-IDF** (Term Frequency-Inverse Document Frequency) technique. The search engine ranks documents based on their relevance to the user's query. It uses libraries like `sklearn`, `pandas`, and `tkinter` to create a basic but functional search system.

## Repo Structure

```
.gitignore
.pre-commit-config.yaml
Main.py
README.md
data_description.txt
requirements.txt
ml-exercise.Naseeb.Grewal.bundle
```

### File Descriptions:
- **.gitignore**: Specifies which files and directories to ignore when committing to Git.
- **.pre-commit-config.yaml**: Contains pre-commit hooks configuration to ensure code quality.
- **Main.py**: The main Python file to execute the search engine.
- **README.md**: This file, providing an overview of the project.
- **data_description.txt**: A description of the data used in the project.
- **requirements.txt**: Lists the dependencies required to run the project.
- **ml-exercise.Naseeb.Grewal.bundle**: Bundle for the exercise (possibly containing data or configurations related to the project).

## Steps to Execute the Service

### Step 1: Clone or Download the Repository

- **Option 1:** Clone the repository using Git:
  ```bash
  git clone https://github.com/yourusername/SmallSearchEngineUsingTF-IDF.git
  ```

- **Option 2:** Alternatively, download the following files:
  - `Main.py`
  - `df_queries.csv` *(Please ensure both files are in the same directory)*

  You can download the `df_queries.csv` file from the following link:
  [Download df_queries.csv](https://drive.google.com/file/d/1SMidi8j6shCwgeHIeSzncSEdtYdF5r4q/view?usp=sharing)

### Step 2: Install Dependencies

Ensure that the following libraries are installed in your environment:

- **sklearn**
- **pandas**
- **tkinter**

To install them, use the following command:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Execute the `Main.py` file to initiate the service:
```bash
python Main.py
```

After running the program, the application will prompt you to enter a query. Upon pressing the "Search Query" button, the program will display the 10 most relevant documents based on the TF-IDF ranking.

## Limitations and Future Improvements

The model used in this project has certain limitations, such as:

- The TF-IDF model is relatively simple and does not account for semantic meaning or context of the query.
- It may not perform well with very large datasets or complex queries.

### Potential Improvements:
- Implementing more advanced models such as **word embeddings** or **BERT** for better semantic search capabilities.
- Adding a **user interface (UI)** for a more interactive experience.
- Improving query ranking with **machine learning models** trained specifically for search tasks.

For further details, refer to the `Q/A.txt` file, which explains the model's limitations and suggests ways to improve its accuracy.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project! Open an issue or submit a pull request if you'd like to improve the search engine or suggest additional features.
```

This structure is clear and provides step-by-step instructions while keeping the formatting clean and readable for others. You can adjust specific details like repository links and license if necessary.
