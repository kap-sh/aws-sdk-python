"""Generated from Smithy shape ``com.amazonaws.apprunner#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.tag_key
    import aws_sdk_apprunner.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_apprunner.types.tag_key.TagKey"]
    """<p>The key of the tag.</p>"""
    value: NotRequired["aws_sdk_apprunner.types.tag_value.TagValue"]
    """<p>The value of the tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
