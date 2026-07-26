"""Generated from Smithy shape ``com.amazonaws.quicksight#SessionTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.session_tag

SessionTagList: TypeAlias = list["capo_quicksight.types.session_tag.SessionTag"]


# --- restJson1 ser/de ---
def serialize_json(value: SessionTagList) -> list:
    import capo_quicksight.types.session_tag

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.session_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionTagList:
    import capo_quicksight.types.session_tag

    out: SessionTagList = []
    for item in data:
        out.append(capo_quicksight.types.session_tag.deserialize_json(item))
    return out
