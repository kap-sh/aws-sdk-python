"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceStateDetailCode``."""

from typing import Literal, TypeAlias, cast

ContainerServiceStateDetailCode: TypeAlias = Literal[
    "CREATING_SYSTEM_RESOURCES",
    "CREATING_NETWORK_INFRASTRUCTURE",
    "PROVISIONING_CERTIFICATE",
    "PROVISIONING_SERVICE",
    "CREATING_DEPLOYMENT",
    "EVALUATING_HEALTH_CHECK",
    "ACTIVATING_DEPLOYMENT",
    "CERTIFICATE_LIMIT_EXCEEDED",
    "UNKNOWN_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceStateDetailCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceStateDetailCode:
    return cast(ContainerServiceStateDetailCode, data)
