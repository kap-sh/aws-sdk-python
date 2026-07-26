"""Generated from Smithy shape ``com.amazonaws.sagemaker#BooleanOperator``."""

from typing import Literal, TypeAlias, cast

BooleanOperator: TypeAlias = Literal[
    "And",
    "Or",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BooleanOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BooleanOperator:
    return cast(BooleanOperator, data)
