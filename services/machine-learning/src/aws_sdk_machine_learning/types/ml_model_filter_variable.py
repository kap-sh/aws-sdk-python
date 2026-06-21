"""Generated from Smithy shape ``com.amazonaws.machinelearning#MLModelFilterVariable``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: MLModelFilterVariable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MLModelFilterVariable:
    return cast(MLModelFilterVariable, data)
