from flask import *


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", jd=None, resume=None, jd_skills=[], soft_skills=[], skill_gap=[], show_results=False)


@app.route('/run_model', methods=['POST'])
def run_model():
    if (request.form['submit_button'] == 'home'):
        return redirect(url_for('index'))
    jd = request.form['jd']
    resume = request.form['resume']
    print(jd, resume)
    jd_skills = ["java", "python"]
    soft_skills = ["leadership", "teanwork"]
    skill_gap = ["excel"]
    return render_template("index.html", jd=jd, resume=resume, jd_skills=jd_skills, soft_skills=soft_skills, skill_gap=skill_gap, show_results=True)


if __name__ == "__main__":
    app.run(debug=True)
