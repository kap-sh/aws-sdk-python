"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

ReplicationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationStatus:
    return cast(ReplicationStatus, data)
