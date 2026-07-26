"""Generated from Smithy shape ``com.amazonaws.mediatailor#FunctionMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.event_name

FunctionMapping: TypeAlias = dict[
    "capo_mediatailor.types.event_name.EventName",
    "capo_mediatailor.types.__string.__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FunctionMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_mediatailor.types.event_name

        out[capo_mediatailor.types.event_name.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> FunctionMapping:
    out: FunctionMapping = {}
    for key, value in data.items():
        import capo_mediatailor.types.event_name

        out[capo_mediatailor.types.event_name.deserialize_json(key)] = value
    return out
