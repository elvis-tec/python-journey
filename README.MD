# 🐍 python-journey

> **Exploring the Python universe without a map but with plenty of caffeine. 🚀**
>
> This repository is a living log of my learning process. It covers everything from the "Hello World" basics to my first steps into Data Analysis and Machine Learning. 

⚠️ **Warning:** Code in 'learning mode' ahead. Expect messy scripts, constant refactoring, and lots of comments!

---

## 🗺️ The Roadmap

I'm following a path to transition from a Python beginner to a Data-focused developer.

### 🐳 Docker Setup (Recommended)

To keep the environment clean and isolated, I'm using Docker. This ensures consistent dependencies and avoids cluttering my local machine.

1.  **Start the Container:**
    ```bash
    docker compose up -d
    ```

2.  **Enter the Container:**
    ```bash
    docker compose exec app bash
    ```
    *From here, you can run python scripts like `python 01_basics/hello_world.py`*
    *or run a python script and exit the container: `docker compose exec app python 01_basics/hello_world.py`*

3.  **Stop the Container:**
    ```bash
    docker compose down
    ```

### Phase 1: Python Fundamentals 🧱
- [ ] **Basic Syntax:** Variables, Data Types (Strings, Integers, Floats).
- [ ] **Control Flow:** If/Else statements and logical operators.
- [ ] **Loops:** For & While loops.
- [ ] **Data Structures:** Lists, Tuples, Sets, and Dictionaries.
- [ ] **Functions:** Defining functions, arguments, and return values.

### Phase 2: Intermediate Python & Tools ⚙️
- [ ] **File I/O:** Reading and writing CSV/JSON files.
- [ ] **Error Handling:** Try/Except blocks.
- [ ] **Modules & Packages:** Using `pip` and importing libraries.
- [ ] **Virtual Environments:** Keeping projects isolated (venv/conda).

### Phase 3: The Data Path 📊 (Future Goals)
- [ ] **NumPy:** Mathematical operations and arrays.
- [ ] **Pandas:** Data manipulation (Cleaning and Analyzing DataFrames).
- [ ] **Matplotlib / Seaborn:** Data Visualization.
- [ ] **Scikit-Learn:** My first Machine Learning models.

---

## 📂 Project Structure

To keep things organized, I’m using the following folder structure:

* `01_basics/`: Early scripts and syntax exercises.
* `02_intermediate/`: More complex logic and data handling.
* `projects/`: Small real-world applications.
* `resources/`: Links to tutorials, books, or documentation I found helpful.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **IDE:** VS Code
* **Environment:** Git & GitHub

---

## ✍️ Author
**[Elvis]** *Feel free to reach out if you have tips for a fellow learner!*