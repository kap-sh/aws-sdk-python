"""Generated from Smithy shape ``com.amazonaws.glue#PartitionIndexStatus``."""

from typing import Literal, TypeAlias, cast

PartitionIndexStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionIndexStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartitionIndexStatus:
    return cast(PartitionIndexStatus, data)
