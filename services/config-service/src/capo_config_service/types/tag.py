"""Generated from Smithy shape ``com.amazonaws.configservice#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.tag_key
    import capo_config_service.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_config_service.types.tag_key.TagKey"]
    """<p>One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.</p>"""
    value: NotRequired["capo_config_service.types.tag_value.TagValue"]
    """<p>The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
