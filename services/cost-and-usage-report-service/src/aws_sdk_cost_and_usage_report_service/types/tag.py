"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.tag_key
    import aws_sdk_cost_and_usage_report_service.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_cost_and_usage_report_service.types.tag_key.TagKey"
    """<p>The key of the tag. Tag keys are case sensitive. Each report definition can only have up to one tag with the same key. If you try to add an existing tag with the same key, the existing tag value will be updated to the new value.</p>"""
    value: "aws_sdk_cost_and_usage_report_service.types.tag_value.TagValue"
    """<p>The value of the tag. Tag values are case-sensitive. This can be an empty string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Tag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
