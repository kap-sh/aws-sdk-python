"""Generated from Smithy shape ``com.amazonaws.sfn#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.tag_key
    import capo_sfn.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_sfn.types.tag_key.TagKey"]
    """<p>The key of a tag.</p>"""
    value: NotRequired["capo_sfn.types.tag_value.TagValue"]
    """<p>The value of a tag.</p>"""


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
