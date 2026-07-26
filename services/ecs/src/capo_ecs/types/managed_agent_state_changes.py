"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgentStateChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.managed_agent_state_change

ManagedAgentStateChanges: TypeAlias = list[
    "capo_ecs.types.managed_agent_state_change.ManagedAgentStateChange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAgentStateChanges) -> list:
    import capo_ecs.types.managed_agent_state_change

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.managed_agent_state_change.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedAgentStateChanges:
    import capo_ecs.types.managed_agent_state_change

    out: ManagedAgentStateChanges = []
    for item in data:
        out.append(
            capo_ecs.types.managed_agent_state_change.deserialize_aws_json_1_1(item)
        )
    return out
