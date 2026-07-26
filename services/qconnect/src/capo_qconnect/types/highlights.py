"""Generated from Smithy shape ``com.amazonaws.qconnect#Highlights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.highlight

Highlights: TypeAlias = list["capo_qconnect.types.highlight.Highlight"]


# --- restJson1 ser/de ---
def serialize_json(value: Highlights) -> list:
    import capo_qconnect.types.highlight

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.highlight.serialize_json(item))
    return out


def deserialize_json(data: list) -> Highlights:
    import capo_qconnect.types.highlight

    out: Highlights = []
    for item in data:
        out.append(capo_qconnect.types.highlight.deserialize_json(item))
    return out
