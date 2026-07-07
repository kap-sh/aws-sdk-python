"""Generated from Smithy shape ``com.amazonaws.opensearch#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.tag_key
    import aws_sdk_opensearch.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_opensearch.types.tag_key.TagKey"
    """<p>The tag key. Tag keys must be unique for the domain to which they are attached.</p>"""
    value: "aws_sdk_opensearch.types.tag_value.TagValue"
    """<p>The value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key value pair in a tag set of <code>project : Trinity</code> and <code>cost-center : Trinity</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Tag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
