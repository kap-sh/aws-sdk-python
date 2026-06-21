"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceMetadataState``."""

from typing import Literal, TypeAlias, cast

InstanceMetadataState: TypeAlias = Literal[
    "pending",
    "applied",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceMetadataState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceMetadataState:
    return cast(InstanceMetadataState, data)
