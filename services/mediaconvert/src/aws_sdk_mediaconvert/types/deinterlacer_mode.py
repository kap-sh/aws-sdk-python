"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DeinterlacerMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Deinterlacer to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive."""
DeinterlacerMode: TypeAlias = Literal[
    "DEINTERLACE",
    "INVERSE_TELECINE",
    "ADAPTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEINTERLACE",
        "INVERSE_TELECINE",
        "ADAPTIVE",
    )
)


def serialize_json(value: DeinterlacerMode) -> str:
    return value


def deserialize_json(data: str) -> DeinterlacerMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeinterlacerMode value: {data!r}")
    return cast(DeinterlacerMode, data)
