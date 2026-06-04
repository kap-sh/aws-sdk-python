"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_agent

ManagedAgents: TypeAlias = list["aws_sdk_ecs.types.managed_agent.ManagedAgent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAgents) -> list:
    import aws_sdk_ecs.types.managed_agent

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.managed_agent.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedAgents:
    import aws_sdk_ecs.types.managed_agent

    out: ManagedAgents = []
    for item in data:
        out.append(aws_sdk_ecs.types.managed_agent.deserialize_aws_json_1_1(item))
    return out
