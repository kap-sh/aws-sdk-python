"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.tag_key
    import capo_application_signals.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_application_signals.types.tag_key.TagKey"
    """<p>A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.</p>"""
    value: "capo_application_signals.types.tag_value.TagValue"
    """<p>The value for the specified tag key.</p>"""


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
