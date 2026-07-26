"""Generated from Smithy shape ``com.amazonaws.eventbridge#ReplicationState``."""

from typing import Literal, TypeAlias, cast

ReplicationState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationState:
    return cast(ReplicationState, data)
