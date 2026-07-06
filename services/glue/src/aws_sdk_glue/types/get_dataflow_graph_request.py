"""Generated from Smithy shape ``com.amazonaws.glue#GetDataflowGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.python_script


class GetDataflowGraphRequest(TypedDict, closed=True):
    python_script: NotRequired["aws_sdk_glue.types.python_script.PythonScript"]
    """<p>The Python script to transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataflowGraphRequest) -> dict:
    out: dict = {}
    if "python_script" in value:
        out["PythonScript"] = value["python_script"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataflowGraphRequest:
    out: GetDataflowGraphRequest = {}  # type: ignore[typeddict-item]
    if "PythonScript" in data:
        out["python_script"] = data["PythonScript"]
    return out
