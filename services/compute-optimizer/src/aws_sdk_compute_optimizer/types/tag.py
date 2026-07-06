"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.tag_key
    import aws_sdk_compute_optimizer.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_compute_optimizer.types.tag_key.TagKey"]
    """<p> One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values. </p>"""
    value: NotRequired["aws_sdk_compute_optimizer.types.tag_value.TagValue"]
    """<p> One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
