"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineStatus``."""

from typing import Literal, TypeAlias, cast

StateMachineStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StateMachineStatus:
    return cast(StateMachineStatus, data)
