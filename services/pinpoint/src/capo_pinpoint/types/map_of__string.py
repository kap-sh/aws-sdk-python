"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOf__string``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string

MapOf__string: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string", "capo_pinpoint.types.__string.__string"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOf__string) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MapOf__string:
    out: MapOf__string = {}
    for key, value in data.items():
        out[key] = value
    return out
