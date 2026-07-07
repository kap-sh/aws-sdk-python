"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowTypeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.name
    import aws_sdk_swf.types.version_optional


class WorkflowTypeFilter(TypedDict, closed=True):
    name: "aws_sdk_swf.types.name.Name"
    """<p> Name of the workflow type.</p>"""
    version: NotRequired["aws_sdk_swf.types.version_optional.VersionOptional"]
    """<p>Version of the workflow type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTypeFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowTypeFilter:
    out: WorkflowTypeFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkflowTypeFilter.name required")
    if "version" in data:
        out["version"] = data["version"]
    return out
