"""Generated from Smithy shape ``com.amazonaws.medialive#CdiInputResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Maximum CDI input resolution; SD is 480i and 576i up to 30 frames-per-second (fps), HD is 720p up to 60 fps / 1080i up to 30 fps, FHD is 1080p up to 60 fps, UHD is 2160p up to 60 fps"""
CdiInputResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "FHD",
    "UHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SD",
        "HD",
        "FHD",
        "UHD",
    )
)


def serialize_json(value: CdiInputResolution) -> str:
    return value


def deserialize_json(data: str) -> CdiInputResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CdiInputResolution value: {data!r}")
    return cast(CdiInputResolution, data)
