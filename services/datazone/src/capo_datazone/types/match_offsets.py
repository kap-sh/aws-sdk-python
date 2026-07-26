"""Generated from Smithy shape ``com.amazonaws.datazone#MatchOffsets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.match_offset

MatchOffsets: TypeAlias = list["capo_datazone.types.match_offset.MatchOffset"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchOffsets) -> list:
    import capo_datazone.types.match_offset

    out: list = []
    for item in value:
        out.append(capo_datazone.types.match_offset.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchOffsets:
    import capo_datazone.types.match_offset

    out: MatchOffsets = []
    for item in data:
        out.append(capo_datazone.types.match_offset.deserialize_json(item))
    return out
