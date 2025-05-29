# 🦸‍♂️🦹‍♀️ Superhero Data Scraper 

For superheroes, villains, antiheroes, and everyone in between, this one's for the geeks!

Ever wondered who’s your bet in a head-to-head — Batman 🦇 or Iron Man 🤖?  
Ever thought being a billionaire might actually increase your odds of becoming a superhero? 💸  
Can gender, occupation, and power stats predict who saves the day — or destroys it? 😈

This project's purpose is to scrape data from the [Superhero API](https://superheroapi.com), bringing your comic book and cinematic universe favorites into the world of data science, econometrics, and analytics! 📊💥

## 📁 Repo structure 

Here's what you'll find in this repo:
```
  DataMining-Superheroes/
  ├── README.md  # Project overview 📖
  ├── .gitignore # Files Git should totally ignore 🚫
  ├── environment.yml # Conda environment with all required libraries (pinned versions) 🐍
  ├── code/
  │   └── datamining.py #  Main script that scrapes superhero data and processes it 🕵️‍♂️ 
  └── data/
      └── superheroes.csv  # Final dataset with the collected superhero data as a CSV file 🦸‍♂️
  ```
## 🚀 How to run the project? 

Ready to dive into your superhero data adventure? Just follow these quick steps:

### 1. 📥 Clone the repo 
```bash
git clone https://github.com/your-username/DataMining-Superheroes.git
```
### 2. 🛠️ Set up the virtual environment 

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
### 3. 🔐 API Access Token & .env File

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

Saves the collected data as a CSV file in `data/superheroes.csv` 📊

🦸‍♀️ Sit back, relax, and let your favorite heroes (and villains) fill up your dataset!

## 📚 Variables Dictionary

Here's your guide to the columns in the dataset 🔍: 

| Variable         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `id`             | Unique ID assigned to each character 🆔                                    |
| `superhero_name` | The public alias or superhero/villain name 🦹‍♀️🦸‍♂️                         |
| `real_name`      | The character's true identity behind the mask 🎭                            |
| `publisher`      | Comic universe or publisher (e.g., Marvel, DC) 🏢                          |
| `alignment`      | Good 😇, bad 😈, or neutral 😐                         |
| `gender`         | Gender identity 🚻                                                         |
| `race`           | Species or racial background (e.g., Human, Kryptonian) 👽                  |
| `occupation`     | Their job when they’re not saving (or destroying) the world 💼             |
| `intelligence`   | Measured brainpower 🧠                                                     |
| `strength`       | Raw physical strength 💪                                                   |
| `speed`          | How fast they move ⚡                                                     |
| `durability`     | Ability to resist damage 🛡️                                               |
| `power`          | Overall superpower rating 🔮                                               |
| `combat`         | Fighting skills and martial arts mastery 👊                               |
| `image_url`      | Link to the character’s portrait image 🖼️                                 |
| `api_url`        | Direct URL to the character’s JSON data endpoint 🌐                         |

Unleash your inner data hero and start exploring! 🧙‍♂️📊🦸

## 🙌 Acknowledgments

Big thanks to the real heroes behind this project! 🦸‍♂️🦸‍♀️

- The [Superhero API team](https://superheroapi.com) for sharing an awesome accessible data source!  
- Open source devs and the Python community for all their amazing tools 🐍   
- And of course, YOU — thanks for checking this out and joining in the fun! 🚀


