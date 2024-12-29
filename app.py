from flask import Flask,redirect,render_template,url_for,request
import random
app=Flask(__name__)

todo=[
    {
        'id':1,
        'name':'eating',
        'done':False
    },
     {
        'id':2,
        'name':'sleeping',
        'done':True
    },
    {
        'id':3,
        'name':'gardening',
        'done':False
    }
]
@app.route('/',methods=["POST","GET"])
@app.route('/home',methods=["POST","GET"])
def home():
    if(request.method=="POST"):
        todo_name=request.form['todoname'].strip() 
        if todo_name:
            ids=random.randint(1,1000)
            todo.append(
                {
                    'id':ids,
                    'name':todo_name,
                    'done':False
                }
                )
    return render_template('index.html',todo=todo)

@app.route('/checked/<int:todo_id>',methods=["POST"])
def checked_todo(todo_id):
    for task in todo:
        if task['id']==todo_id:
            task['done']=not task['done']
            break
    return redirect(url_for('home'))

@app.route('/delete/<int:todo_id>',methods=["POST"])
def delete_todo(todo_id):
    global todos
    for task in todo:
        if todo_id==task['id']:
            todo.remove(task)
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)