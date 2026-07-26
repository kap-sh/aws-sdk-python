"""Generated from Smithy shape ``com.amazonaws.gamelift#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.tag_key
    import capo_gamelift.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_gamelift.types.tag_key.TagKey"]
    """<p>The key for a developer-defined key value pair for tagging an Amazon Web Services resource. </p>"""
    value: NotRequired["capo_gamelift.types.tag_value.TagValue"]
    """<p>The value for a developer-defined key value pair for tagging an Amazon Web Services resource. </p>"""


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
