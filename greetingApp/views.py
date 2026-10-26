from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random

# Create your views here.
STYLE = """
<style>
    body { font-family: Arial, sans-serif; background: #eef2f7; margin: 0; }
    .card { max-width: 650px; margin: 40px auto; padding: 30px; background: #fff;
            border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
    h1 { color: #1a5276; margin-top: 0; }
    .quote { font-style: italic; border-left: 4px solid #1a5276;
             padding-left: 12px; margin: 20px 0; }
    nav a { margin-right: 14px; font-weight: bold; color: #1a5276; text-decoration: none; }
    ul { line-height: 1.8; }
</style>
"""

NAV = """
<nav>
    <a href="/greeting/">Greeting</a>
    <a href="/welcome/">Welcome</a>
    <a href="/motivation/">Motivation</a>
    <a href="/time/">Time</a>
    <a href="/date/">Date</a>
    <a href="/worldclock/">World Clock</a>
</nav>
<hr>
"""

QUOTES = [
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
]


def greetings_view(request):
    # Greeting changes automatically with the server's hour
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting, emoji = "Good Morning", "☀️"
    elif hour < 16:
        greeting, emoji = "Good Afternoon", "🌤️"
    else:
        greeting, emoji = "Good Evening", "🌙"

    html = f"""
    <div class="card">
        <h1>{emoji} Hello Friends, {greeting}!</h1>
        <p>Have a nice day. This greeting was chosen by Python based on the
           current server hour (<b>{hour}:00</b>).</p>
        <p>Refresh this page at different times of the day and the message
           will change on its own.</p>
    </div>
    """
    return HttpResponse(html)


def welcome_view(request):
    html = f"""
    <div class="card">
        <h1>👋 Welcome to Our Django Project</h1>
        <p>This project contains <b>two applications</b> working together:</p>
        <ul>
            <li><b>greetingApp</b> - greeting, welcome and motivation pages</li>
            <li><b>timeApp</b> - current time, date details and world clock</li>
        </ul>
        <p>Each app has its own <code>views.py</code>, but all URLs are
           registered in the project's single <code>urls.py</code>.</p>
        <p>Use the links above to move between pages from both apps.</p>
    </div>
    """
    return HttpResponse(html)


def birthday_view(request):
    today = datetime.date.today()

    # Enter your birthday month and day here
    birthday_month = 10
    birthday_day = 25

    # Calculate the next birthday
    next_birthday = datetime.date(
        today.year, birthday_month, birthday_day
    )

    if next_birthday < today:
        next_birthday = datetime.date(
            today.year + 1, birthday_month, birthday_day
        )

    days_left = (next_birthday - today).days

    html = f"""
        <html>
        <head>
            <title>Birthday Page</title>
        </head>
        <body style="font-family: Arial; background-color: lightpink;
                     padding: 40px; text-align: center;">

            <h1>🎂 Happy Birthday!</h1>

            <p>Your next birthday is on
               {next_birthday.strftime("%d %B %Y")}.</p>

            <h2>{days_left} days until your next birthday!</h2>

        </body>
        </html>
    """

    return HttpResponse(html)
