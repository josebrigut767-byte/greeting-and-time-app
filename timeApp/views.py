from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
STYLE = """
<style>
    body { font-family: Arial, sans-serif; background: #1c2833; color: #ecf0f1; margin: 0; }
    .card { max-width: 650px; margin: 40px auto; padding: 30px; background: #273746;
            border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); }
    h1 { color: #f5b041; margin-top: 0; }
    .big { font-size: 42px; font-weight: bold; color: #f5b041; }
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    td, th { padding: 8px; border-bottom: 1px solid #566573; text-align: left; }
    nav a { margin-right: 14px; font-weight: bold; color: #f5b041; text-decoration: none; }
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


def time_info_view(request):
    now = datetime.datetime.now()
    html = f"""
    <div class="card">
        <h1>⏰ Hello, Current Date and Time</h1>
        <p class="big">{now.strftime("%I:%M:%S %p")}</p>
        <p>{now.strftime("%A, %d %B %Y")}</p>
        <p>Raw Python value: <code>{now}</code></p>
        <p>Refresh the page to see the time update. Each request runs the
           view again and reads a fresh value from the server clock.</p>
    </div>
    """
    return HttpResponse(html)


def date_info_view(request):
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    days_left = (new_year - today).days
    day_of_year = today.timetuple().tm_yday
    week_number = today.isocalendar()[1]
    is_weekend = "Yes 🎉" if today.weekday() >= 5 else "No, it's a working day"

    html = f"""
    <div class="card">
        <h1>📅 Date Details</h1>
        <table>
            <tr><th>Item</th><th>Value</th></tr>
            <tr><td>Today's date</td><td>{today.strftime("%d/%m/%Y")}</td></tr>
            <tr><td>Day of the week</td><td>{today.strftime("%A")}</td></tr>
            <tr><td>Month</td><td>{today.strftime("%B")}</td></tr>
            <tr><td>Day of the year</td><td>{day_of_year}</td></tr>
            <tr><td>Week number</td><td>{week_number}</td></tr>
            <tr><td>Is it the weekend?</td><td>{is_weekend}</td></tr>
            <tr><td>Days until New Year</td><td>{days_left}</td></tr>
        </table>
    </div>
    """
    return HttpResponse(html)


def world_clock_view(request):
    # Fixed UTC offsets (in hours) - no extra packages needed
    cities = [
    ("Lagos, Nigeria", 1),
    ("London, UK", 0),
    ("New York, USA", -5),
    ("Dubai, UAE", 4),
    ("New Delhi, India", 5.5),
    ("Tokyo, Japan", 9),

    # Nine additional countries
    ("Accra, Ghana", 0),
    ("Nairobi, Kenya", 3),
    ("Cairo, Egypt", 2),
    ("Johannesburg, South Africa", 2),
    ("Riyadh, Saudi Arabia", 3),
    ("Singapore", 8),
    ("Bangkok, Thailand", 7),
    ("Beijing, China", 8),
    ("Sydney, Australia", 10),
]
    utc_now = datetime.datetime.now(datetime.timezone.utc)

    rows = ""
    for city, offset in cities:
        city_time = utc_now + datetime.timedelta(hours=offset)
        rows += f"<tr><td>{city}</td><td>UTC{offset:+g}</td><td>{city_time.strftime('%I:%M %p')}</td></tr>"

    html = f"""
    <div class="card">
        <h1>🌍 World Clock</h1>
        <table>
            <tr><th>City</th><th>Offset</th><th>Time</th></tr>
            {rows}
        </table>
        <p style="font-size:13px;">Note: offsets are fixed and do not adjust
           for daylight saving time.</p>
    </div>
    """
    return HttpResponse(html)