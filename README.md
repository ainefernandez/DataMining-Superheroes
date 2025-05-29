# 🦸‍♂️🦹‍♀️ Superhero Data Scraper 

For superheroes, villains, antiheroes, and everyone in between — this one's for the geeks!

Ever wondered who’s your bet in a head-to-head — Batman 🦇 or Iron Man 🤖?  
Ever thought being a billionaire might actually increase your odds of becoming a superhero? 💸  
Can gender, occupation, and power stats predict who saves the day — or destroys it? 😈

This project's purpose is to scrape data from the [Superhero API](https://superheroapi.com), bringing your comic book and cinematic universe favorites into the world of data science, econometrics, and analytics! 📊💥

## 📁 Repo structure 

Here's what you'll find in this repo:
```
  DataMining-Superheroes/
  ├── README.md  # Project overview 📖
  ├── .gitignore # Files and folders to ignore by git 🚫
  ├── environment.yml # Conda environment with all required libraries (pinned versions) 🐍
  ├── code/
  │   └── datamining.py #  Main script that scrapes superhero data and processes it 🕵️‍♂️ 
  └── data/
      └── superheroes.csv  # Final dataset with the collected superhero data as a CSV file 🦸‍♂️
  ```
## 🚀 How to run the project? 

Ready to dive into your superhero data adventure? Just follow these quick steps:

### 1. Clone the repo 📥  
```bash
git clone https://github.com/your-username/DataMining-Superheroes.git
```
### 2. Set up the virtual environment 🛠️

Make sure you have Conda installed ✅

Then, create the environment by running:
```bash
conda env create -f environment.yml
```

Activate your new superhero scraper environment: 

```bash
conda activate superhero-scraper
```

To deactivate the environment, just run: 
```bash
conda deactivate 
```
### 3. 🔐 API Access Token & `.env` File

To fetch data from the Superhero API, you’ll need an access token. Don’t worry, it’s quick, easy, and free!

🧑‍💻 **Step 1**: Make sure you have a valid GitHub account.  
🔗 **Step 2**: Head over to [Superhero API](https://superheroapi.com) and generate your personal access token.

⚠️ **Important**: This token is private and should **never** be shared or pushed to GitHub.

To keep your token safe and run the scripts **without exposing it**, follow these steps:

1. Create a `.env` file in the root directory:
```bash
touch .env
```
2. Open the .env file and add your access token like this:
```env
   access_token=your_access_token_here
```
🦸‍♂️ That’s it! Just like a superhero's secret identity, your access token will stay safe, far away from the evils of data leakage!

### 4. 🕷️ Scrape the Data!

Ready to dive into the superhero multiverse? Let’s get that data! 🌌

Make sure your virtual environment is activated 🧪  
Then run the scraping script:

```bash
python code/datamining.py
```
🛠️ What this script does:

Loops through all character IDs in the API (from 1 to 731) 🆔

Constructs a record for each character 🧬

Ignores any characters with missing power stats — because we need the full picture of our heroes' and villains' abilities! 💥

Saves the final dataset as a CSV file in the `data/` folder 🧾

🦸‍♀️ Sit back, relax, and let your favorite heroes (and villains) fill up your dataset!
