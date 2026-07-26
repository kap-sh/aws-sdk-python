"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthCheckType``."""

from typing import Literal, TypeAlias, cast

HealthCheckType: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
    "TCP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheckType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthCheckType:
    return cast(HealthCheckType, data)
