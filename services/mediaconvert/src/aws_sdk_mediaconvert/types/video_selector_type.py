"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the video selector type for your HLS input. Use to specify which video rendition MediaConvert uses from your HLS input. To have MediaConvert automatically use the highest bitrate rendition from your HLS input: Keep the default value, Auto. To manually specify a rendition: Choose Stream. Then enter the unique stream number in the Streams array, starting at 1, corresponding to the stream order in the manifest."""
VideoSelectorType: TypeAlias = Literal[
    "AUTO",
    "STREAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "STREAM",
    )
)


def serialize_json(value: VideoSelectorType) -> str:
    return value


def deserialize_json(data: str) -> VideoSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoSelectorType value: {data!r}")
    return cast(VideoSelectorType, data)
