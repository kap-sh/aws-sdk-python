"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

StreamProcessorStatus: TypeAlias = Literal[
    "STOPPED",
    "STARTING",
    "RUNNING",
    "FAILED",
    "STOPPING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STOPPED",
        "STARTING",
        "RUNNING",
        "FAILED",
        "STOPPING",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: StreamProcessorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamProcessorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamProcessorStatus value: {data!r}")
    return cast(StreamProcessorStatus, data)
