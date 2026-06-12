"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MediaUriType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

MediaUriType: TypeAlias = Literal[
    "RTSP_URI",
    "FILE_URI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RTSP_URI",
        "FILE_URI",
    )
)


def serialize_json(value: MediaUriType) -> str:
    return value


def deserialize_json(data: str) -> MediaUriType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaUriType value: {data!r}")
    return cast(MediaUriType, data)
