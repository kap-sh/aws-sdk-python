"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When you have a progressive segmented frame (PsF) input, use this setting to flag the input as PsF. MediaConvert doesn't automatically detect PsF. Therefore, flagging your input as PsF results in better preservation of video quality when you do deinterlacing and frame rate conversion. If you don't specify, the default value is Auto. Auto is the correct setting for all inputs that are not PsF. Don't set this value to PsF when your input is interlaced. Doing so creates horizontal interlacing artifacts."""
InputScanType: TypeAlias = Literal[
    "AUTO",
    "PSF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "PSF",
    )
)


def serialize_json(value: InputScanType) -> str:
    return value


def deserialize_json(data: str) -> InputScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputScanType value: {data!r}")
    return cast(InputScanType, data)
