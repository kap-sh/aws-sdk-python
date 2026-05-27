"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_agent_name
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedAgent(TypedDict):
    last_started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the managed agent was last started.</p>"""
    name: NotRequired["aws_sdk_ecs.types.managed_agent_name.ManagedAgentName"]
    """<p>The name of the managed agent. When the execute command feature is turned on, the managed agent name is <code>ExecuteCommandAgent</code>.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for why the managed agent is in the state it is in.</p>"""
    last_status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The last known status of the managed agent.</p>"""
