"""Generated from Smithy shape ``com.amazonaws.imagebuilder#EbsVolumeType``."""

from typing import Literal, TypeAlias, cast

EbsVolumeType: TypeAlias = Literal[
    "standard",
    "io1",
    "io2",
    "gp2",
    "gp3",
    "sc1",
    "st1",
]


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumeType) -> str:
    return value


def deserialize_json(data: str) -> EbsVolumeType:
    return cast(EbsVolumeType, data)
