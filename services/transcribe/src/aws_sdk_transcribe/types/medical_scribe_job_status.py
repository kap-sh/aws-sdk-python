"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

MedicalScribeJobStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: MedicalScribeJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MedicalScribeJobStatus value: {data!r}")
    return cast(MedicalScribeJobStatus, data)
