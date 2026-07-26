"""Generated from Smithy shape ``com.amazonaws.odb#OperationsInsightsStatus``."""

from typing import Literal, TypeAlias, cast

OperationsInsightsStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "NOT_ENABLED",
    "FAILED_ENABLING",
    "FAILED_DISABLING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OperationsInsightsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationsInsightsStatus:
    return cast(OperationsInsightsStatus, data)
