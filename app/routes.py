from app import app
from flask import render_template, request, redirect
from app.models import model, formopener

@app.route('/')
@app.route('/index', methods = ['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/reset", methods = ['GET', 'POST'])
def reset():
    if request.method == "POST" or request.method =="GET":
        model.resetGrid()
        return redirect('/play_game')

@app.route('/play_game', methods = ['GET','POST'])
def play_game():
    grid = model.grid
    playerId = request.args.get("id")
    boxNum = request.args.get("boxNum")
    
    if boxNum != None:
        boxNum = int(boxNum)
        model.makeMark(playerId, boxNum)
        
    if playerId == None:
        nextTurn = "X"
    if playerId == "O":
        nextTurn = "X"
    if playerId == "X":
        nextTurn = "O"
    
    gameCheck = model.isWinner(grid, playerId)
    
    print(gameCheck)
    if gameCheck == "X wins!":
        return "X IS THE WINNER!"
    elif gameCheck == "O wins!":
        return "O IS THE WINNER"
    else:
        return render_template("play_game.html", grid=grid, playerId=playerId, nextTurn=nextTurn)

