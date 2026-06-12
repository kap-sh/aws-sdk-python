"""Generated from Smithy shape ``com.amazonaws.rekognition#VideoJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

VideoJobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: VideoJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VideoJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoJobStatus value: {data!r}")
    return cast(VideoJobStatus, data)
