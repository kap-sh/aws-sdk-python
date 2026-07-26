"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptionJobStatus``."""

from typing import Literal, TypeAlias, cast

TranscriptionJobStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranscriptionJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TranscriptionJobStatus:
    return cast(TranscriptionJobStatus, data)
