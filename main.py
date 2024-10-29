from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static folder if you want to add CSS files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Keep track of input and result
current_input = ""

@app.get("/", response_class=HTMLResponse)
async def calculator():
    # HTML code for the calculator interface
    html_content = f"""
    <html>
        <head>
            <title>Calculator</title>
            <style>
                body {{ display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Arial; }}
                .calculator {{ width: 200px; text-align: center; }}
                .display {{ height: 30px; margin-bottom: 10px; font-size: 1.5em; text-align: right; padding-right: 10px; }}
                .buttons {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 5px; }}
                button {{ font-size: 1.2em; padding: 10px; }}
            </style>
        </head>
        <body>
            <div class="calculator">
                <div class="display">{current_input}</div>
                <form method="post" class="buttons">
                    <button type="submit" name="input" value="1">1</button>
                    <button type="submit" name="input" value="2">2</button>
                    <button type="submit" name="input" value="3">3</button>
                    <button type="submit" name="input" value="+">+</button>
                    <button type="submit" name="input" value="4">4</button>
                    <button type="submit" name="input" value="5">5</button>
                    <button type="submit" name="input" value="6">6</button>
                    <button type="submit" name="input" value="-">-</button>
                    <button type="submit" name="input" value="7">7</button>
                    <button type="submit" name="input" value="8">8</button>
                    <button type="submit" name="input" value="9">9</button>
                    <button type="submit" name="input" value="*">*</button>
                    <button type="submit" name="input" value="0">0</button>
                    <button type="submit" name="input" value="C">C</button>
                    <button type="submit" name="input" value="=">=</button>
                    <button type="submit" name="input" value="/">/</button>
                </form>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/", response_class=HTMLResponse)
async def calculate(input: str = Form(...)):
    global current_input

    if input == "=":
        try:
            # Evaluate the expression
            current_input = str(eval(current_input))
        except:
            current_input = "Error"
    elif input == "C":
        # Clear the input
        current_input = ""
    else:
        # Append the input to the current expression
        current_input += input

    return await calculator()
