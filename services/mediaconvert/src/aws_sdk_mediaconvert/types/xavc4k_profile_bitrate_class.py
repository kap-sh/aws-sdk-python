"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kProfileBitrateClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
Xavc4kProfileBitrateClass: TypeAlias = Literal[
    "BITRATE_CLASS_100",
    "BITRATE_CLASS_140",
    "BITRATE_CLASS_200",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BITRATE_CLASS_100",
        "BITRATE_CLASS_140",
        "BITRATE_CLASS_200",
    )
)


def serialize_json(value: Xavc4kProfileBitrateClass) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kProfileBitrateClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Xavc4kProfileBitrateClass value: {data!r}")
    return cast(Xavc4kProfileBitrateClass, data)
