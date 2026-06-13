"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemeridesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemeris_item

EphemeridesList: TypeAlias = list[
    "aws_sdk_groundstation.types.ephemeris_item.EphemerisItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemeridesList) -> list:
    import aws_sdk_groundstation.types.ephemeris_item

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.ephemeris_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> EphemeridesList:
    import aws_sdk_groundstation.types.ephemeris_item

    out: EphemeridesList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.ephemeris_item.deserialize_json(item))
    return out
