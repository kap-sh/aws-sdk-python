"""Generated from Smithy shape ``com.amazonaws.odb#IormLifecycleState``."""

from typing import Literal, TypeAlias, cast

IormLifecycleState: TypeAlias = Literal[
    "BOOTSTRAPPING",
    "DISABLED",
    "ENABLED",
    "FAILED",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IormLifecycleState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IormLifecycleState:
    return cast(IormLifecycleState, data)
