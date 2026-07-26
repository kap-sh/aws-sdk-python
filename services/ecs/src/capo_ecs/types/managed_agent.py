"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.managed_agent_name
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ManagedAgent(TypedDict, closed=True):
    last_started_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the managed agent was last started.</p>"""
    name: NotRequired["capo_ecs.types.managed_agent_name.ManagedAgentName"]
    """<p>The name of the managed agent. When the execute command feature is turned on, the managed agent name is <code>ExecuteCommandAgent</code>.</p>"""
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason for why the managed agent is in the state it is in.</p>"""
    last_status: NotRequired["capo_ecs.types.string.String"]
    """<p>The last known status of the managed agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAgent) -> dict:
    out: dict = {}
    if "last_started_at" in value:
        import capo_ecs.types.timestamp

        out["lastStartedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["last_started_at"]
        )
    if "name" in value:
        import capo_ecs.types.managed_agent_name

        out["name"] = capo_ecs.types.managed_agent_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "last_status" in value:
        out["lastStatus"] = value["last_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedAgent:
    out: ManagedAgent = {}  # type: ignore[typeddict-item]
    if "lastStartedAt" in data:
        import capo_ecs.types.timestamp

        out["last_started_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["lastStartedAt"]
        )
    if "name" in data:
        import capo_ecs.types.managed_agent_name

        out["name"] = capo_ecs.types.managed_agent_name.deserialize_aws_json_1_1(
            data["name"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    if "lastStatus" in data:
        out["last_status"] = data["lastStatus"]
    return out
