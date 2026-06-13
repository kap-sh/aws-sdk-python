"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.tag_key
    import aws_sdk_compute_optimizer_automation.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_compute_optimizer_automation.types.tag_key.TagKey"
    """<p>The tag key, which can be up to 128 characters long.</p>"""
    value: "aws_sdk_compute_optimizer_automation.types.tag_value.TagValue"
    """<p>The tag value, which can be up to 256 characters long.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
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
