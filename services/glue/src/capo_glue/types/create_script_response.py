"""Generated from Smithy shape ``com.amazonaws.glue#CreateScriptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.python_script
    import capo_glue.types.scala_code


class CreateScriptResponse(TypedDict, closed=True):
    python_script: NotRequired["capo_glue.types.python_script.PythonScript"]
    """<p>The Python script generated from the DAG.</p>"""
    scala_code: NotRequired["capo_glue.types.scala_code.ScalaCode"]
    """<p>The Scala code generated from the DAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScriptResponse) -> dict:
    out: dict = {}
    if "python_script" in value:
        out["PythonScript"] = value["python_script"]
    if "scala_code" in value:
        out["ScalaCode"] = value["scala_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScriptResponse:
    out: CreateScriptResponse = {}  # type: ignore[typeddict-item]
    if "PythonScript" in data:
        out["python_script"] = data["PythonScript"]
    if "ScalaCode" in data:
        out["scala_code"] = data["ScalaCode"]
    return out
