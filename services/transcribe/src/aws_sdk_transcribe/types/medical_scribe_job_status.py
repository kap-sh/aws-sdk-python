"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeJobStatus``."""

from typing import Literal, TypeAlias, cast

MedicalScribeJobStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeJobStatus:
    return cast(MedicalScribeJobStatus, data)
