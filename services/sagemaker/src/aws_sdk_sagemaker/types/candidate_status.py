"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateStatus``."""

from typing import Literal, TypeAlias, cast

CandidateStatus: TypeAlias = Literal[
    "Completed",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CandidateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CandidateStatus:
    return cast(CandidateStatus, data)
