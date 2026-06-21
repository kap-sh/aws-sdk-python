"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#HealthStatusCode``."""

from typing import Literal, TypeAlias, cast

HealthStatusCode: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HealthStatusCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HealthStatusCode:
    return cast(HealthStatusCode, data)
