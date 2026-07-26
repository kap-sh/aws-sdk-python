"""Generated from Smithy shape ``com.amazonaws.iot#ClientProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.string

ClientProperties: TypeAlias = dict[
    "capo_iot.types.string.String", "capo_iot.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ClientProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ClientProperties:
    out: ClientProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
