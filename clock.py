from datetime import timedelta
from streamlit.components.v1 import html


def add_clock(length: timedelta = timedelta(hours=1)):
    num_seconds = length.total_seconds()
    html(
        """
    <h1>Time Remaining:</h1>
    <div class="time">
    <a class="hours">
    <a class="minutes">
    <a class="seconds">
    </div>
    <script>
    function getTimeRemaining(endtime) {
    const total = Date.parse(endtime) - Date.parse(new Date());
    const seconds = Math.floor((total / 1000) % 60);
    const minutes = Math.floor((total / 1000 / 60) % 60);
    const hours = Math.floor((total / (1000 * 60 * 60)) % 24);

    return {
        total,
        hours,
        minutes,
        seconds
    };
    }

    function initializeClock(endtime) {
    const hoursDiv = document.querySelector('.hours');
    const minutesDiv = document.querySelector('.minutes');
    const secondsDiv = document.querySelector('.seconds');

    function updateClock() {
        const t = getTimeRemaining(endtime);

        hoursDiv.innerHTML = ('0' + t.hours).slice(-2) + ' hours ';
        minutesDiv.innerHTML = ('0' + t.minutes).slice(-2) + ' minutes ';
        secondsDiv.innerHTML = ('0' + t.seconds).slice(-2) + ' seconds ';

        if (t.total <= 0) {
        clearInterval(timeinterval);
        }
    }

    updateClock();
    const timeinterval = setInterval(updateClock, 1000);
    }
    """
        + f"const deadline = new Date(Date.parse(new Date()) + {num_seconds} * 1000);"
        + """
    initializeClock(deadline);
    </script>
    <style>
    body{
    text-align: center;
    background: #00ECB9;
    font-family: sans-serif;
    display: inline-block;
    font-weight: 100;
    }
 

    h1{
    color: #000;
    float:left;
    font-weight: 100;
    font-size: 20px;
    margin: 10px 0px 0px;
    }

    .time{
    color: #000;
    float:left;
    font-weight: 100;
    font-size: 20px;
    margin: 10px 40px 40px;
    }

 
    </style>
    """,
        height=60,
    )


