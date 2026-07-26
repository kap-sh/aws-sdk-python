"""Generated from Smithy shape ``com.amazonaws.quicksight#SessionTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.session_tag_key

SessionTagKeyList: TypeAlias = list[
    "capo_quicksight.types.session_tag_key.SessionTagKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionTagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> SessionTagKeyList:
    return list(data)
