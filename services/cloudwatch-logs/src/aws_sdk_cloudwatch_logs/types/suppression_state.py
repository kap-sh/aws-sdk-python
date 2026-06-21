"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SuppressionState``."""

from typing import Literal, TypeAlias, cast

SuppressionState: TypeAlias = Literal[
    "SUPPRESSED",
    "UNSUPPRESSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuppressionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuppressionState:
    return cast(SuppressionState, data)
