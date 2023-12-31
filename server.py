from flask import Flask ,render_template,url_for, request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')



def write_csv(data):
    with open('database.csv',newline='', mode ='a') as database2:
        name= data["name"]
        email = data["email"]
        message= data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])


@app.route('/contact', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect('/')
        except:
            return "didnt save to database"
    else:
        return"lacking"
    
if __name__ == '__main__':
    app.run(debug=True)