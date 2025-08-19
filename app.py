from flask import Flask, render_template, request
import random

app = Flask(__name__)

# generate random number at app start
target = random.randint(1, 10)

@app.route("/", methods=["GET", "POST"])
def home():
    global target
    message = ""
    
    if request.method == "POST":
        user_choice = request.form.get("guess")
        
        # Quit button
        if user_choice.upper() == "Q":
            message = "Game Over! The correct number was " + str(target)
            target = random.randint(1, 100)  # reset game
        else:
            try:
                guess = int(user_choice)
                if guess == target:
                    message = f"🎉 Correct! {guess} is the number."
                    target = random.randint(1, 10)  # reset new game
                elif guess < target:
                    message = "Too small! Try a bigger number."
                else:
                    message = "Too large! Try a smaller number."
            except:
                message = "Please enter a valid number."
    
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)