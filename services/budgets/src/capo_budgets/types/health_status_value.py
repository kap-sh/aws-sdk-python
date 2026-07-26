"""Generated from Smithy shape ``com.amazonaws.budgets#HealthStatusValue``."""

from typing import Literal, TypeAlias, cast

HealthStatusValue: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthStatusValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthStatusValue:
    return cast(HealthStatusValue, data)
