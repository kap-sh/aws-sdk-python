"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeLifecycle``."""

from typing import Literal, TypeAlias, cast

VolumeLifecycle: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "FAILED",
    "MISCONFIGURED",
    "PENDING",
    "AVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeLifecycle:
    return cast(VolumeLifecycle, data)
