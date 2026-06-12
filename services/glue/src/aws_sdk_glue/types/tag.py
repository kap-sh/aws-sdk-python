"""Generated from Smithy shape ``com.amazonaws.glue#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.tag_key
    import aws_sdk_glue.types.tag_value


class Tag(TypedDict):
    key: NotRequired["aws_sdk_glue.types.tag_key.TagKey"]
    """<p>The tag key. The key is required when you create a tag on an object. The key is case-sensitive, and must not contain the prefix aws.</p>"""
    value: NotRequired["aws_sdk_glue.types.tag_value.TagValue"]
    """<p>The tag value. The value is optional when you create a tag on an object. The value is case-sensitive, and must not contain the prefix aws.</p>"""


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
