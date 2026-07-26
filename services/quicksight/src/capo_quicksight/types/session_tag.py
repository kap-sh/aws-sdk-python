"""Generated from Smithy shape ``com.amazonaws.quicksight#SessionTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.session_tag_key
    import capo_quicksight.types.session_tag_value


class SessionTag(TypedDict, closed=True):
    key: "capo_quicksight.types.session_tag_key.SessionTagKey"
    """<p>The key for the tag.</p>"""
    value: "capo_quicksight.types.session_tag_value.SessionTagValue"
    """<p>The value that you want to assign the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionTag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SessionTag:
    out: SessionTag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("SessionTag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("SessionTag.value required")
    return out
