"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgentName``."""

from typing import Literal, TypeAlias, cast

ManagedAgentName: TypeAlias = Literal["ExecuteCommandAgent",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAgentName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedAgentName:
    return cast(ManagedAgentName, data)
