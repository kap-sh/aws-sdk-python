"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3StereoDownmix``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose how the service does stereo downmixing. This setting only applies if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Stereo downmix."""
Eac3StereoDownmix: TypeAlias = Literal[
    "NOT_INDICATED",
    "LO_RO",
    "LT_RT",
    "DPL2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_INDICATED",
        "LO_RO",
        "LT_RT",
        "DPL2",
    )
)


def serialize_json(value: Eac3StereoDownmix) -> str:
    return value


def deserialize_json(data: str) -> Eac3StereoDownmix:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3StereoDownmix value: {data!r}")
    return cast(Eac3StereoDownmix, data)
