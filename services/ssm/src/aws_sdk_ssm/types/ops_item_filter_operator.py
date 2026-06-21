"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemFilterOperator``."""

from typing import Literal, TypeAlias, cast

OpsItemFilterOperator: TypeAlias = Literal[
    "Equal",
    "Contains",
    "GreaterThan",
    "LessThan",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemFilterOperator:
    return cast(OpsItemFilterOperator, data)
