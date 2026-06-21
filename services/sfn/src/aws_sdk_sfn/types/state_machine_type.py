"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineType``."""

from typing import Literal, TypeAlias, cast

StateMachineType: TypeAlias = Literal[
    "STANDARD",
    "EXPRESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StateMachineType:
    return cast(StateMachineType, data)
