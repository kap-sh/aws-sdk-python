"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateSortBy``."""

from typing import Literal, TypeAlias, cast

CandidateSortBy: TypeAlias = Literal[
    "CreationTime",
    "Status",
    "FinalObjectiveMetricValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CandidateSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CandidateSortBy:
    return cast(CandidateSortBy, data)
