"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptionJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

TranscriptionJobStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: TranscriptionJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TranscriptionJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscriptionJobStatus value: {data!r}")
    return cast(TranscriptionJobStatus, data)
