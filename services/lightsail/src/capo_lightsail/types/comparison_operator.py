"""Generated from Smithy shape ``com.amazonaws.lightsail#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
