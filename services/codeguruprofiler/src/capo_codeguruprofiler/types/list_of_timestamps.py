"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListOfTimestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.timestamp_structure

ListOfTimestamps: TypeAlias = list[
    "capo_codeguruprofiler.types.timestamp_structure.TimestampStructure"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTimestamps) -> list:
    import capo_codeguruprofiler.types.timestamp_structure

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.timestamp_structure.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTimestamps:
    import capo_codeguruprofiler.types.timestamp_structure

    out: ListOfTimestamps = []
    for item in data:
        out.append(
            capo_codeguruprofiler.types.timestamp_structure.deserialize_json(item)
        )
    return out
