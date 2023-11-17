import os

from dotenv import load_dotenv
from flask import request, render_template, abort

from kafp1910_app import create_app
from kafp1910_app.controllers import create_form_data, form_data_list, retrieve_form_controller

load_dotenv()
app = create_app(os.getenv("CONFIG_MODE"))


@app.route("/")
def home():
    page = request.args.get('page', 1, type=int)

    return form_data_list(page=page)


@app.route("/forms/", methods=["GET", "POST"])
def create_list_forms():
    if request.method == "POST":
        return create_form_data()

    return render_template("create_data.html")


@app.route("/forms/<int:form_id>/", methods=["GET"])
def retrieve_form(form_id: int):
    if request.method == "GET":
        form_data = retrieve_form_controller(form_id)

        return render_template("form_info.html", **{"form_obj": form_data})
    return abort(405)


if __name__ == '__main__':
    app.run()
