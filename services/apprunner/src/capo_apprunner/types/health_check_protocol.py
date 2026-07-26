"""Generated from Smithy shape ``com.amazonaws.apprunner#HealthCheckProtocol``."""

from typing import Literal, TypeAlias, cast

HealthCheckProtocol: TypeAlias = Literal[
    "TCP",
    "HTTP",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HealthCheckProtocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HealthCheckProtocol:
    return cast(HealthCheckProtocol, data)
