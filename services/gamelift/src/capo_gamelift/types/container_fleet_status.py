"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetStatus``."""

from typing import Literal, TypeAlias, cast

ContainerFleetStatus: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "CREATED",
    "ACTIVATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerFleetStatus:
    return cast(ContainerFleetStatus, data)
