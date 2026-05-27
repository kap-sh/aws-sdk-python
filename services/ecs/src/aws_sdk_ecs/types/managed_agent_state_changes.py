"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgentStateChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_agent_state_change

ManagedAgentStateChanges: TypeAlias = list[
    "aws_sdk_ecs.types.managed_agent_state_change.ManagedAgentStateChange"
]
