# Pandasai-MongoDB-Analysis

Integration of **PandasAI** with **MongoDB** to enable natural language data analysis on MongoDB collections using pandas-powered workflows.

This project demonstrates how to connect to a MongoDB database, convert the data into a Pandas DataFrame, and then use **PandasAI** with **DeepSeek LLM** for natural language queries.

---

## 📂 Project Structure

```
cache/  
.env  
.env.sample  
.gitignore  
main.py  
pandasai.log  
pyproject.toml  
.python-version  
README.md  
uv.lock  
.venv/
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/ezratechdev/Pandasai-MongoDB-Analysis.git
   cd Pandasai-MongoDB-Analysis
   ```

2. **Copy environment file**  
   ```bash
   cp .env.sample .env
   ```
   Update the values in `.env` with your MongoDB and DeepSeek credentials.

   Example:
   ```env
   mongo_string=mongodb+srv://<user>:<password>@cluster0.mongodb.net
   database=my_database
   collection=my_collection
   api_base=https://api.deepseek.com/v1
   api_token=your_deepseek_api_key
   model=deepseek-chat
   ```

3. **Install [uv](https://github.com/astral-sh/uv)**  
   Follow the installation guide from the docs.

4. **Install Python 3.11 (works best with PandasAI)**  
   ```bash
   uv python install 3.11
   ```

5. **Initialize uv project**  
   ```bash
   uv init
   ```

6. **Create virtual environment**  
   ```bash
   uv venv --python 3.11
   ```

7. **Activate virtual environment**  
   ```bash
   source .venv/bin/activate
   ```

8. **Install dependencies**  
   ```bash
   uv sync
   ```

9. **Run the script**  
   ```bash
   uv run main.py
   ```

---

## 🧠 How It Works

- Connects to MongoDB via the `mongo_string` URI.  
- Reads a collection into a Pandas DataFrame.  
- Drops the default `_id` column.  
- Uses **PandasAI SmartDataFrame** with a custom `DeepSeekLLM` connector.  
- Example query:
  ```
  What is the average value of amount
  ```

---

## 📝 Notes

- **DeepSeek** was used as the LLM provider for PandasAI integration.  
- Make sure your MongoDB collection has numerical fields if you want to run aggregation queries like averages.  
- Logs are written to `pandasai.log`.  

---

## 🔮 Example Output

```bash
> uv run main.py
42.3
```

Where `42.3` is the computed result from your MongoDB dataset.

---

### PS:
This README was enhanced using AI
