from django.http import HttpResponse
import random


def motivation_view(request):
    quotes = [
        ("The secret of getting ahead is getting started.", "Mark Twain"),
        ("It always seems impossible until it's done.", "Nelson Mandela"),
        ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
        ("Talk is cheap. Show me the code.", "Linus Torvalds"),
        ("First, solve the problem. Then, write code.", "John Johnson"),
    ]

    quote, author = random.choice(quotes)

    return HttpResponse(f"""
        <h1>Quote of the Moment</h1>
        <p><i>"{quote}"</i></p>
        <p>— {author}</p>
        <a href="/motivation/">Get another quote</a>
        <br><br>
        <a href="/greeting/">Back to Greeting</a>
    """)