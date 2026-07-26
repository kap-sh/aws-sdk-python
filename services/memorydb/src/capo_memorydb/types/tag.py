"""Generated from Smithy shape ``com.amazonaws.memorydb#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_memorydb.types.string.String"]
    """<p>The key for the tag. May not be null.</p>"""
    value: NotRequired["capo_memorydb.types.string.String"]
    """<p>The tag's value. May be null.</p>"""


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
