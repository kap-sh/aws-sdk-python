"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSourceByteRateLimit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose whether to limit the byte rate at which your SCC input captions are inserted into your output. To not limit the caption rate: We recommend that you keep the default value, Disabled. MediaConvert inserts captions in your output according to the byte rates listed in the EIA-608 specification, typically 2 or 3 caption bytes per frame depending on your output frame rate. To limit your output caption rate: Choose Enabled. Choose this option if your downstream systems require a maximum of 2 caption bytes per frame. Note that this setting has no effect when your output frame rate is 30 or 60."""
CaptionSourceByteRateLimit: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: CaptionSourceByteRateLimit) -> str:
    return value


def deserialize_json(data: str) -> CaptionSourceByteRateLimit:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CaptionSourceByteRateLimit value: {data!r}"
        )
    return cast(CaptionSourceByteRateLimit, data)
