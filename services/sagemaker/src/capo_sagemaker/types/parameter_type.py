"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParameterType``."""

from typing import Literal, TypeAlias, cast

ParameterType: TypeAlias = Literal[
    "Integer",
    "Continuous",
    "Categorical",
    "FreeText",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterType:
    return cast(ParameterType, data)
