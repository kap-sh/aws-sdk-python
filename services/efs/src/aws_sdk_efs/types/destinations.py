"""Generated from Smithy shape ``com.amazonaws.efs#Destinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_efs.types.destination

Destinations: TypeAlias = list["aws_sdk_efs.types.destination.Destination"]


# --- restJson1 ser/de ---
def serialize_json(value: Destinations) -> list:
    import aws_sdk_efs.types.destination

    out: list = []
    for item in value:
        out.append(aws_sdk_efs.types.destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> Destinations:
    import aws_sdk_efs.types.destination

    out: Destinations = []
    for item in data:
        out.append(aws_sdk_efs.types.destination.deserialize_json(item))
    return out
