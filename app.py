from flask import Flask, render_template, request

app = Flask(__name__)
MY_SKILLS = [
    "Python",
    "Git",
    "Flask",
    "HTML",
    "CSS"
]

@app.route("/", methods=["GET", "POST"])
def index():
    found_skills = []
    matched_skills = []
    missing_skills = []

    match_rate = 0
    bar_color = "red"

    if request.method == "POST":

        job_text = request.form.get("job_text", "")

        skills = [
            "Python",
            "SQL",
            "Git",
            "Flask",
            "AWS",
            "Docker",
            "HTML",
            "CSS"
        ]

        for skill in skills:
            if skill.lower() in job_text.lower():
                found_skills.append(skill)

        for skill in found_skills:
            if skill in MY_SKILLS:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        if len(found_skills) > 0:
            match_rate = round(
                len(matched_skills) / len(found_skills) * 100
            )

        if match_rate >= 80:
            bar_color = "green"
        elif match_rate >= 50:
            bar_color = "orange"
        else:
            bar_color = "red"

    return render_template(
        "index.html",
        found_skills=found_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        match_rate=match_rate,
        bar_color=bar_color
    )

if __name__ == "__main__":
    app.run(debug=True)
