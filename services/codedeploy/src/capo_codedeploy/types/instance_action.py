"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceAction``."""

from typing import Literal, TypeAlias, cast

InstanceAction: TypeAlias = Literal[
    "TERMINATE",
    "KEEP_ALIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceAction:
    return cast(InstanceAction, data)
