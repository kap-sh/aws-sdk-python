"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LogDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_simspaceweaver.types.log_destination

LogDestinations: TypeAlias = list[
    "capo_simspaceweaver.types.log_destination.LogDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogDestinations) -> list:
    import capo_simspaceweaver.types.log_destination

    out: list = []
    for item in value:
        out.append(capo_simspaceweaver.types.log_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogDestinations:
    import capo_simspaceweaver.types.log_destination

    out: LogDestinations = []
    for item in data:
        out.append(capo_simspaceweaver.types.log_destination.deserialize_json(item))
    return out
