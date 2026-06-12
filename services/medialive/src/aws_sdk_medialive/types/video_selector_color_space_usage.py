"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorColorSpaceUsage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Video Selector Color Space Usage"""
VideoSelectorColorSpaceUsage: TypeAlias = Literal[
    "FALLBACK",
    "FORCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FALLBACK",
        "FORCE",
    )
)


def serialize_json(value: VideoSelectorColorSpaceUsage) -> str:
    return value


def deserialize_json(data: str) -> VideoSelectorColorSpaceUsage:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VideoSelectorColorSpaceUsage value: {data!r}"
        )
    return cast(VideoSelectorColorSpaceUsage, data)
