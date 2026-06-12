"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsStreamInfResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest."""
HlsStreamInfResolution: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: HlsStreamInfResolution) -> str:
    return value


def deserialize_json(data: str) -> HlsStreamInfResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsStreamInfResolution value: {data!r}")
    return cast(HlsStreamInfResolution, data)
