"""Generated from Smithy shape ``com.amazonaws.machinelearning#MLModelType``."""

from typing import Literal, TypeAlias, cast

MLModelType: TypeAlias = Literal[
    "REGRESSION",
    "BINARY",
    "MULTICLASS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MLModelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MLModelType:
    return cast(MLModelType, data)
