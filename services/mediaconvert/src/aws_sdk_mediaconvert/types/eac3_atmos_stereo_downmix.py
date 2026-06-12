"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosStereoDownmix``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose how the service does stereo downmixing. Default value: Not indicated Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Stereo downmix."""
Eac3AtmosStereoDownmix: TypeAlias = Literal[
    "NOT_INDICATED",
    "STEREO",
    "SURROUND",
    "DPL2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_INDICATED",
        "STEREO",
        "SURROUND",
        "DPL2",
    )
)


def serialize_json(value: Eac3AtmosStereoDownmix) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosStereoDownmix:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3AtmosStereoDownmix value: {data!r}")
    return cast(Eac3AtmosStereoDownmix, data)
