"""Generated from Smithy shape ``com.amazonaws.glue#CreateScriptResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.python_script
    import aws_sdk_glue.types.scala_code


class CreateScriptResponse(TypedDict):
    python_script: NotRequired["aws_sdk_glue.types.python_script.PythonScript"]
    """<p>The Python script generated from the DAG.</p>"""
    scala_code: NotRequired["aws_sdk_glue.types.scala_code.ScalaCode"]
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
