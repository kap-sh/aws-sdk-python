"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceProtocol``."""

from typing import Literal, TypeAlias, cast

ContainerServiceProtocol: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceProtocol:
    return cast(ContainerServiceProtocol, data)
