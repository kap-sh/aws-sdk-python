"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedDraining``."""

from typing import Literal, TypeAlias, cast

ManagedDraining: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedDraining) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedDraining:
    return cast(ManagedDraining, data)
