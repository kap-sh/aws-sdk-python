"""Generated from Smithy shape ``com.amazonaws.glue#SessionCommand``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.python_version_string


class SessionCommand(TypedDict):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Specifies the name of the SessionCommand. Can be 'glueetl' or 'gluestreaming'.</p>"""
    python_version: NotRequired[
        "aws_sdk_glue.types.python_version_string.PythonVersionString"
    ]
    """<p>Specifies the Python version. The Python version indicates the version supported for jobs of type Spark.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionCommand) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "python_version" in value:
        out["PythonVersion"] = value["python_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionCommand:
    out: SessionCommand = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "PythonVersion" in data:
        out["python_version"] = data["PythonVersion"]
    return out
