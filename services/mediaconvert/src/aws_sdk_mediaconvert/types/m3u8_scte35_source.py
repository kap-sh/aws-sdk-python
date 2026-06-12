"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M3u8Scte35Source``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None if you don't want manifest conditioning. Choose Passthrough and choose Ad markers if you do want manifest conditioning. In both cases, also provide the ESAM XML as a string in the setting Signal processing notification XML."""
M3u8Scte35Source: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "NONE",
    )
)


def serialize_json(value: M3u8Scte35Source) -> str:
    return value


def deserialize_json(data: str) -> M3u8Scte35Source:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M3u8Scte35Source value: {data!r}")
    return cast(M3u8Scte35Source, data)
