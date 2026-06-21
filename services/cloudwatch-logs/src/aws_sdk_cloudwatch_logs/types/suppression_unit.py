"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SuppressionUnit``."""

from typing import Literal, TypeAlias, cast

SuppressionUnit: TypeAlias = Literal[
    "SECONDS",
    "MINUTES",
    "HOURS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuppressionUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuppressionUnit:
    return cast(SuppressionUnit, data)
