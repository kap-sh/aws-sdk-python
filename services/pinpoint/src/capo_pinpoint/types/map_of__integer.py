"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOf__integer``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string

MapOf__integer: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string", "capo_pinpoint.types.__integer.__integer"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOf__integer) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MapOf__integer:
    out: MapOf__integer = {}
    for key, value in data.items():
        out[key] = value
    return out
