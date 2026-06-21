"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#HealthCheckProtocol``."""

from typing import Literal, TypeAlias, cast

HealthCheckProtocol: TypeAlias = Literal[
    "TCP",
    "HTTP",
    "HTTPS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheckProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthCheckProtocol:
    return cast(HealthCheckProtocol, data)
