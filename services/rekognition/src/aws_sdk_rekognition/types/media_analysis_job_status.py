"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

MediaAnalysisJobStatus: TypeAlias = Literal[
    "CREATED",
    "QUEUED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "QUEUED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: MediaAnalysisJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MediaAnalysisJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaAnalysisJobStatus value: {data!r}")
    return cast(MediaAnalysisJobStatus, data)
