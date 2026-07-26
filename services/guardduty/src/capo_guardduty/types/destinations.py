"""Generated from Smithy shape ``com.amazonaws.guardduty#Destinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.destination

Destinations: TypeAlias = list["capo_guardduty.types.destination.Destination"]


# --- restJson1 ser/de ---
def serialize_json(value: Destinations) -> list:
    import capo_guardduty.types.destination

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> Destinations:
    import capo_guardduty.types.destination

    out: Destinations = []
    for item in data:
        out.append(capo_guardduty.types.destination.deserialize_json(item))
    return out
