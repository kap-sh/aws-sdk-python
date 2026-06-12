"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.peering

PeeringList: TypeAlias = list["aws_sdk_networkmanager.types.peering.Peering"]


# --- restJson1 ser/de ---
def serialize_json(value: PeeringList) -> list:
    import aws_sdk_networkmanager.types.peering

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.peering.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeeringList:
    import aws_sdk_networkmanager.types.peering

    out: PeeringList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.peering.deserialize_json(item))
    return out
