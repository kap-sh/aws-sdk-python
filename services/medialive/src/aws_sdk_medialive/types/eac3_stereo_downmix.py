"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3StereoDownmix``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Stereo Downmix"""
Eac3StereoDownmix: TypeAlias = Literal[
    "DPL2",
    "LO_RO",
    "LT_RT",
    "NOT_INDICATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DPL2",
        "LO_RO",
        "LT_RT",
        "NOT_INDICATED",
    )
)


def serialize_json(value: Eac3StereoDownmix) -> str:
    return value


def deserialize_json(data: str) -> Eac3StereoDownmix:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3StereoDownmix value: {data!r}")
    return cast(Eac3StereoDownmix, data)
