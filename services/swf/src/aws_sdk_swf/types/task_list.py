"""Generated from Smithy shape ``com.amazonaws.swf#TaskList``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.name


class TaskList(TypedDict):
    name: "aws_sdk_swf.types.name.Name"
    """<p>The name of the task list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskList) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskList:
    out: TaskList = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TaskList.name required")
    return out
