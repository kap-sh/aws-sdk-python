"""Generated from Smithy shape ``com.amazonaws.iotwireless#DestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.destinations

DestinationList: TypeAlias = list["capo_iot_wireless.types.destinations.Destinations"]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationList) -> list:
    import capo_iot_wireless.types.destinations

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.destinations.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationList:
    import capo_iot_wireless.types.destinations

    out: DestinationList = []
    for item in data:
        out.append(capo_iot_wireless.types.destinations.deserialize_json(item))
    return out
