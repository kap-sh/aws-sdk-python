"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SuppressionType``."""

from typing import Literal, TypeAlias, cast

SuppressionType: TypeAlias = Literal[
    "LIMITED",
    "INFINITE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuppressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuppressionType:
    return cast(SuppressionType, data)
