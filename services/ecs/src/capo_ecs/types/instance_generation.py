"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceGeneration``."""

from typing import Literal, TypeAlias, cast

InstanceGeneration: TypeAlias = Literal[
    "current",
    "previous",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGeneration) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGeneration:
    return cast(InstanceGeneration, data)
