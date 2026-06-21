"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTerminationProtection``."""

from typing import Literal, TypeAlias, cast

ManagedTerminationProtection: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedTerminationProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedTerminationProtection:
    return cast(ManagedTerminationProtection, data)
