"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceState``."""

from typing import Literal, TypeAlias, cast

ContainerServiceState: TypeAlias = Literal[
    "PENDING",
    "READY",
    "RUNNING",
    "UPDATING",
    "DELETING",
    "DISABLED",
    "DEPLOYING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceState:
    return cast(ContainerServiceState, data)
