"""Generated from Smithy shape ``com.amazonaws.organizations#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.tag_key
    import capo_organizations.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_organizations.types.tag_key.TagKey"
    """<p>The key identifier, or name, of the tag.</p>"""
    value: "capo_organizations.types.tag_value.TagValue"
    """<p>The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
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
