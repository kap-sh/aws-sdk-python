"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgentStateChange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_agent_name
    import aws_sdk_ecs.types.string


class ManagedAgentStateChange(TypedDict):
    container_name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the container that's associated with the managed agent.</p>"""
    managed_agent_name: "aws_sdk_ecs.types.managed_agent_name.ManagedAgentName"
    """<p>The name of the managed agent.</p>"""
    status: "aws_sdk_ecs.types.string.String"
    """<p>The status of the managed agent.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the status of the managed agent.</p>"""
