"""Generated from Smithy shape ``com.amazonaws.shield#Limit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.long
    import aws_sdk_shield.types.string


class Limit(TypedDict):
    type: NotRequired["aws_sdk_shield.types.string.String"]
    """<p>The type of protection.</p>"""
    max: "aws_sdk_shield.types.long.Long"
    """<p>The maximum number of protections that can be created for the specified <code>Type</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Limit) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    out["Max"] = value.get("max", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Limit:
    out: Limit = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Max" in data:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    return out
