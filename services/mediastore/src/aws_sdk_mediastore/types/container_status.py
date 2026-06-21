"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerStatus``."""

from typing import Literal, TypeAlias, cast

ContainerStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerStatus:
    return cast(ContainerStatus, data)
