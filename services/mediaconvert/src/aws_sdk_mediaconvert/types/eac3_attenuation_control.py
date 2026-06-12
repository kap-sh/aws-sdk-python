"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AttenuationControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode."""
Eac3AttenuationControl: TypeAlias = Literal[
    "ATTENUATE_3_DB",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTENUATE_3_DB",
        "NONE",
    )
)


def serialize_json(value: Eac3AttenuationControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3AttenuationControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3AttenuationControl value: {data!r}")
    return cast(Eac3AttenuationControl, data)
