"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.managed_agent

ManagedAgents: TypeAlias = list["capo_ecs.types.managed_agent.ManagedAgent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAgents) -> list:
    import capo_ecs.types.managed_agent

    out: list = []
    for item in value:
        out.append(capo_ecs.types.managed_agent.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedAgents:
    import capo_ecs.types.managed_agent

    out: ManagedAgents = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.managed_agent.deserialize_aws_json_1_1(item))
    return out
