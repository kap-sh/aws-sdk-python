"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.destination

DestinationList: TypeAlias = list["capo_ivs_realtime.types.destination.Destination"]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationList) -> list:
    import capo_ivs_realtime.types.destination

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationList:
    import capo_ivs_realtime.types.destination

    out: DestinationList = []
    for item in data:
        out.append(capo_ivs_realtime.types.destination.deserialize_json(item))
    return out
