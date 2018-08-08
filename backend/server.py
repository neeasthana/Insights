from flask import Flask,render_template

# Main index web page
@application.route('/')
def showMachineList():
    return "hello insights app"
    # return render_template('list.html')

# Login

# Get Insights

# Get Daily Insight

# Add new Insight

# Delete Insight

if __name__ == "__main__":
    application.run(host='0.0.0.0')