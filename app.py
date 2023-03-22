from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name = {})

@app.route('/submitData', methods=['POST'])
def submitData():
    data1 = request.form.get('num1')
    data2 = request.form.get('num2')
    data3 = request.form.get('num3')
    data4 = request.form.get('num4')
    data5 = request.form.get('num5')


    print("data type", type(data1))
    print(f"convert data type: Before {type(data1)} After: { type(int(data1))} ")

    subTotal = int(data1) + int(data2) + int(data3) + int(data4) + int(data5)
    print("subTotal", subTotal)
    if percentage := int(subTotal) * (100 / 500):
        print("percentage", percentage)
        # left with database integration
        return render_template("index.html", result = { "percentage": percentage })
    else:
        return render_template("index.html", result = { })


if __name__ == '__main__':
   app.run()