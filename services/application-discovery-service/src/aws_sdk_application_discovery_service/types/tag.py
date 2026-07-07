"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.tag_key
    import aws_sdk_application_discovery_service.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_application_discovery_service.types.tag_key.TagKey"
    """<p>The type of tag on which to filter.</p>"""
    value: "aws_sdk_application_discovery_service.types.tag_value.TagValue"
    """<p>A value for a tag key on which to filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
