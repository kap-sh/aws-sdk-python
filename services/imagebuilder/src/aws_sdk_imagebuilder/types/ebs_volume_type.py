"""Generated from Smithy shape ``com.amazonaws.imagebuilder#EbsVolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "io1",
        "io2",
        "gp2",
        "gp3",
        "sc1",
        "st1",
    )
)


def serialize_json(value: EbsVolumeType) -> str:
    return value


def deserialize_json(data: str) -> EbsVolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EbsVolumeType value: {data!r}")
    return cast(EbsVolumeType, data)
