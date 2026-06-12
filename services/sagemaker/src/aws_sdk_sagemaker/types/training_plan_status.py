"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingPlanStatus: TypeAlias = Literal[
    "Pending",
    "Active",
    "Scheduled",
    "Expired",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Active",
        "Scheduled",
        "Expired",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: TrainingPlanStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingPlanStatus value: {data!r}")
    return cast(TrainingPlanStatus, data)
