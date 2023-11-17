from flask import request, render_template

from . import db
from .models import FormData


def form_data_list(page: int):
    pagination = FormData.query.paginate(page=page, per_page=5)

    return render_template("main.html", pagination=pagination)


def create_form_data():
    request_form = request.form.to_dict()

    new_instance = FormData(data=request_form)

    db.session.add(new_instance)
    db.session.commit()

    context = {
        "form_obj": new_instance
    }

    return render_template("form_info.html", **context)


def retrieve_form_controller(form_id: int):
    return FormData.query.get_or_404(form_id)
