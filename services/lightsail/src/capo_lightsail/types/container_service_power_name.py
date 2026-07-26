"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicePowerName``."""

from typing import Literal, TypeAlias, cast

ContainerServicePowerName: TypeAlias = Literal[
    "nano",
    "micro",
    "small",
    "medium",
    "large",
    "xlarge",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServicePowerName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServicePowerName:
    return cast(ContainerServicePowerName, data)
