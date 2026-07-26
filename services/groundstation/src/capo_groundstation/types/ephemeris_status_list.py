"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.ephemeris_status

EphemerisStatusList: TypeAlias = list[
    "capo_groundstation.types.ephemeris_status.EphemerisStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisStatusList) -> list:
    import capo_groundstation.types.ephemeris_status

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.ephemeris_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> EphemerisStatusList:
    import capo_groundstation.types.ephemeris_status

    out: EphemerisStatusList = []
    for item in data:
        out.append(capo_groundstation.types.ephemeris_status.deserialize_json(item))
    return out
