"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CandidateSortBy: TypeAlias = Literal[
    "CreationTime",
    "Status",
    "FinalObjectiveMetricValue",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreationTime",
        "Status",
        "FinalObjectiveMetricValue",
    )
)


def serialize_aws_json_1_1(value: CandidateSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CandidateSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CandidateSortBy value: {data!r}")
    return cast(CandidateSortBy, data)
