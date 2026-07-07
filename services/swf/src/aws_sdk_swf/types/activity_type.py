"""Generated from Smithy shape ``com.amazonaws.swf#ActivityType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.name
    import aws_sdk_swf.types.version


class ActivityType(TypedDict, closed=True):
    name: "aws_sdk_swf.types.name.Name"
    """<p>The name of this activity.</p> <note> <p>The combination of activity type name and version must be unique within a domain.</p> </note>"""
    version: "aws_sdk_swf.types.version.Version"
    """<p>The version of this activity.</p> <note> <p>The combination of activity type name and version must be unique with in a domain.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityType) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityType:
    out: ActivityType = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ActivityType.name required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("ActivityType.version required")
    return out
