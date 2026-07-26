"""Generated from Smithy shape ``com.amazonaws.amp#LoggingDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.logging_destination

LoggingDestinations: TypeAlias = list[
    "capo_amp.types.logging_destination.LoggingDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingDestinations) -> list:
    import capo_amp.types.logging_destination

    out: list = []
    for item in value:
        out.append(capo_amp.types.logging_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> LoggingDestinations:
    import capo_amp.types.logging_destination

    out: LoggingDestinations = []
    for item in data:
        out.append(capo_amp.types.logging_destination.deserialize_json(item))
    return out
