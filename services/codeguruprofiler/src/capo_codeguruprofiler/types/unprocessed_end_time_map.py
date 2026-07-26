"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UnprocessedEndTimeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.list_of_timestamps

UnprocessedEndTimeMap: TypeAlias = dict[
    "str", "capo_codeguruprofiler.types.list_of_timestamps.ListOfTimestamps"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UnprocessedEndTimeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codeguruprofiler.types.list_of_timestamps

        out[key] = capo_codeguruprofiler.types.list_of_timestamps.serialize_json(value)
    return out


def deserialize_json(data: dict) -> UnprocessedEndTimeMap:
    out: UnprocessedEndTimeMap = {}
    for key, value in data.items():
        import capo_codeguruprofiler.types.list_of_timestamps

        out[key] = capo_codeguruprofiler.types.list_of_timestamps.deserialize_json(
            value
        )
    return out
