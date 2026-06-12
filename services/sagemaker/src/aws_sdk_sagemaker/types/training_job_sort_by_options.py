"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobSortByOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingJobSortByOptions: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
    "FinalObjectiveMetricValue",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
        "FinalObjectiveMetricValue",
    )
)


def serialize_aws_json_1_1(value: TrainingJobSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingJobSortByOptions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingJobSortByOptions value: {data!r}")
    return cast(TrainingJobSortByOptions, data)
