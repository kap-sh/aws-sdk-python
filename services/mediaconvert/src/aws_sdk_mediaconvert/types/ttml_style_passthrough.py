"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlStylePassthrough``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output."""
TtmlStylePassthrough: TypeAlias = Literal[
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


def serialize_json(value: TtmlStylePassthrough) -> str:
    return value


def deserialize_json(data: str) -> TtmlStylePassthrough:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TtmlStylePassthrough value: {data!r}")
    return cast(TtmlStylePassthrough, data)
