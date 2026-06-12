"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingPlanSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_aws_json_1_1(value: TrainingPlanSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingPlanSortOrder value: {data!r}")
    return cast(TrainingPlanSortOrder, data)
