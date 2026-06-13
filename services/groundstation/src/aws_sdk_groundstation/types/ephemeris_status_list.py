"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemeris_status

EphemerisStatusList: TypeAlias = list[
    "aws_sdk_groundstation.types.ephemeris_status.EphemerisStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisStatusList) -> list:
    import aws_sdk_groundstation.types.ephemeris_status

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.ephemeris_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> EphemerisStatusList:
    import aws_sdk_groundstation.types.ephemeris_status

    out: EphemerisStatusList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.ephemeris_status.deserialize_json(item))
    return out
