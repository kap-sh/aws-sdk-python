"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.destination

DestinationList: TypeAlias = list["aws_sdk_ivs_realtime.types.destination.Destination"]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationList) -> list:
    import aws_sdk_ivs_realtime.types.destination

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs_realtime.types.destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationList:
    import aws_sdk_ivs_realtime.types.destination

    out: DestinationList = []
    for item in data:
        out.append(aws_sdk_ivs_realtime.types.destination.deserialize_json(item))
    return out
