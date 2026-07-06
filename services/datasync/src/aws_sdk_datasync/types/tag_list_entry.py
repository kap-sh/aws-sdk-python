"""Generated from Smithy shape ``com.amazonaws.datasync#TagListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.tag_key
    import aws_sdk_datasync.types.tag_value


class TagListEntry(TypedDict, closed=True):
    key: "aws_sdk_datasync.types.tag_key.TagKey"
    """<p>The key for an Amazon Web Services resource tag.</p>"""
    value: NotRequired["aws_sdk_datasync.types.tag_value.TagValue"]
    """<p>The value for an Amazon Web Services resource tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagListEntry) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagListEntry:
    out: TagListEntry = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("TagListEntry.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    return out
