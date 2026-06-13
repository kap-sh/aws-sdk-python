"""Generated from Smithy shape ``com.amazonaws.location#LegList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.leg

LegList: TypeAlias = list["aws_sdk_location.types.leg.Leg"]


# --- restJson1 ser/de ---
def serialize_json(value: LegList) -> list:
    import aws_sdk_location.types.leg

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.leg.serialize_json(item))
    return out


def deserialize_json(data: list) -> LegList:
    import aws_sdk_location.types.leg

    out: LegList = []
    for item in data:
        out.append(aws_sdk_location.types.leg.deserialize_json(item))
    return out
