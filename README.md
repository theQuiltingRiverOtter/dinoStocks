DinoStocks - Learn About the Stock Market with Dinosaurs!

Overview

DinoStocks is an engaging and educational app designed to introduce kids to the exciting world of the stock market through the fascinating lens of dinosaurs. This app combines the thrill of prehistoric creatures with the fundamentals of finance, providing a unique and entertaining learning experience for young minds.

Features
1. DinoStock Market Simulation
Buy and sell dinosaurs as stocks in a simulated stock market environment.
Experience the volatility of the market with dynamically changing prices.
2. Dino Portfolio Management
Build and manage a portfolio of dinosaur stocks.
Learn the basics of diversification and risk management.
3. Educational Content
Engaging lessons and quizzes to teach financial concepts in a kid-friendly manner.
Learn about investing, dividends, and market trends.
4. Interactive Dinosaur Encyclopedia
Explore a virtual dinosaur encyclopedia with detailed information about each dinosaur.
Connect the characteristics of dinosaurs to stock market concepts.
5. DinoStock Challenges
Complete challenges to earn rewards and enhance financial literacy skills.
Face unique market scenarios and make informed decisions.

To get Celery running after pulling from Github: 
1. makemigrations, migrate, load fixture data for realstonks_app, install requirements.txt (installs celery)
2. Run Redis Server:
    sudo apt-get install redis-server
    sudo service redis-server start
    (Check if running with redis-cli ping. Will return Pong)
    (Stop server with: sudo service redis-server stop)
3. In seperate terminals:
    a. Go into dinostocks/backend and run "python manage.py runserver"
    b. Go into dinostocks/backend and run "celery -A dinostocks_proj worker -l info"
    c. Go into dinostocks/backend and run "celery -A dinostocks_proj beat -l info"
    d. Go into dinostocks/front_end/dino_stocks and run "npm run dev"
    