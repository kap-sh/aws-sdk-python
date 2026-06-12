"""Generated from Smithy shape ``com.amazonaws.machinelearning#MLModelFilterVariable``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_machine_learning.errors import DeserializationError

MLModelFilterVariable: TypeAlias = Literal[
    "CreatedAt",
    "LastUpdatedAt",
    "Status",
    "Name",
    "IAMUser",
    "TrainingDataSourceId",
    "RealtimeEndpointStatus",
    "MLModelType",
    "Algorithm",
    "TrainingDataURI",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreatedAt",
        "LastUpdatedAt",
        "Status",
        "Name",
        "IAMUser",
        "TrainingDataSourceId",
        "RealtimeEndpointStatus",
        "MLModelType",
        "Algorithm",
        "TrainingDataURI",
    )
)


def serialize_aws_json_1_1(value: MLModelFilterVariable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MLModelFilterVariable:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MLModelFilterVariable value: {data!r}")
    return cast(MLModelFilterVariable, data)
