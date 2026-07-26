"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfEvent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.event

MapOfEvent: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string", "capo_pinpoint.types.event.Event"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfEvent) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.event

        out[key] = capo_pinpoint.types.event.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfEvent:
    out: MapOfEvent = {}
    for key, value in data.items():
        import capo_pinpoint.types.event

        out[key] = capo_pinpoint.types.event.deserialize_json(value)
    return out
