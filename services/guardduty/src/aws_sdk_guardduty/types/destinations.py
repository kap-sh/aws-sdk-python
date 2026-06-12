"""Generated from Smithy shape ``com.amazonaws.guardduty#Destinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.destination

Destinations: TypeAlias = list["aws_sdk_guardduty.types.destination.Destination"]


# --- restJson1 ser/de ---
def serialize_json(value: Destinations) -> list:
    import aws_sdk_guardduty.types.destination

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> Destinations:
    import aws_sdk_guardduty.types.destination

    out: Destinations = []
    for item in data:
        out.append(aws_sdk_guardduty.types.destination.deserialize_json(item))
    return out
