"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafStreamInfResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest."""
CmafStreamInfResolution: TypeAlias = Literal[
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


def serialize_json(value: CmafStreamInfResolution) -> str:
    return value


def deserialize_json(data: str) -> CmafStreamInfResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafStreamInfResolution value: {data!r}")
    return cast(CmafStreamInfResolution, data)
