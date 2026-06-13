"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#VideoFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

VideoFormat: TypeAlias = Literal[
    "mkv",
    "mov",
    "mp4",
    "webm",
    "flv",
    "mpeg",
    "mpg",
    "wmv",
    "three_gp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "mkv",
        "mov",
        "mp4",
        "webm",
        "flv",
        "mpeg",
        "mpg",
        "wmv",
        "three_gp",
    )
)


def serialize_json(value: VideoFormat) -> str:
    return value


def deserialize_json(data: str) -> VideoFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoFormat value: {data!r}")
    return cast(VideoFormat, data)
