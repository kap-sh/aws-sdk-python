"""Generated from Smithy shape ``com.amazonaws.ecs#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.tag_key
    import aws_sdk_ecs.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_ecs.types.tag_key.TagKey"]
    """<p>One part of a key-value pair that make up a tag. A <code>key</code> is a general label that acts like a category for more specific tag values.</p>"""
    value: NotRequired["aws_sdk_ecs.types.tag_value.TagValue"]
    """<p>The optional part of a key-value pair that make up a tag. A <code>value</code> acts as a descriptor within a tag category (key).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
