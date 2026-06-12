"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingPlanSortBy: TypeAlias = Literal[
    "TrainingPlanName",
    "StartTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TrainingPlanName",
        "StartTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: TrainingPlanSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingPlanSortBy value: {data!r}")
    return cast(TrainingPlanSortBy, data)
