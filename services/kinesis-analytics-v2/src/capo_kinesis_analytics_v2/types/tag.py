"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.tag_key
    import capo_kinesis_analytics_v2.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_kinesis_analytics_v2.types.tag_key.TagKey"
    """<p>The key of the key-value tag.</p>"""
    value: NotRequired["capo_kinesis_analytics_v2.types.tag_value.TagValue"]
    """<p>The value of the key-value tag. The value is optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
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
    return out
