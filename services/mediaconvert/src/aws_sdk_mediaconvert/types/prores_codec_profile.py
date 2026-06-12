"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProresCodecProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Profile to specify the type of Apple ProRes codec to use for this output."""
ProresCodecProfile: TypeAlias = Literal[
    "APPLE_PRORES_422",
    "APPLE_PRORES_422_HQ",
    "APPLE_PRORES_422_LT",
    "APPLE_PRORES_422_PROXY",
    "APPLE_PRORES_4444",
    "APPLE_PRORES_4444_XQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLE_PRORES_422",
        "APPLE_PRORES_422_HQ",
        "APPLE_PRORES_422_LT",
        "APPLE_PRORES_422_PROXY",
        "APPLE_PRORES_4444",
        "APPLE_PRORES_4444_XQ",
    )
)


def serialize_json(value: ProresCodecProfile) -> str:
    return value


def deserialize_json(data: str) -> ProresCodecProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProresCodecProfile value: {data!r}")
    return cast(ProresCodecProfile, data)
