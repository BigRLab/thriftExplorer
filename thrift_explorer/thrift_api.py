from flask import Blueprint

bp = Blueprint("thrift", __name__, url_prefix="/thrift")


@bp.route("/list", methods=("GET",))
def list_thrifts():
    pass
