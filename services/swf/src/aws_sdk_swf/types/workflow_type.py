"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowType``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.name
    import aws_sdk_swf.types.version


class WorkflowType(TypedDict):
    name: "aws_sdk_swf.types.name.Name"
    """<p> The name of the workflow type.</p> <note> <p>The combination of workflow type name and version must be unique with in a domain.</p> </note>"""
    version: "aws_sdk_swf.types.version.Version"
    """<p> The version of the workflow type.</p> <note> <p>The combination of workflow type name and version must be unique with in a domain.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowType) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowType:
    out: WorkflowType = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkflowType.name required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("WorkflowType.version required")
    return out
