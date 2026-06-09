"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgentStateChange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAgentStateChange) -> dict:
    out: dict = {}
    out["containerName"] = value["container_name"]
    import aws_sdk_ecs.types.managed_agent_name

    out["managedAgentName"] = (
        aws_sdk_ecs.types.managed_agent_name.serialize_aws_json_1_1(
            value["managed_agent_name"]
        )
    )
    out["status"] = value["status"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedAgentStateChange:
    out: ManagedAgentStateChange = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    else:
        raise DeserializationError("ManagedAgentStateChange.container_name required")
    if "managedAgentName" in data:
        import aws_sdk_ecs.types.managed_agent_name

        out["managed_agent_name"] = (
            aws_sdk_ecs.types.managed_agent_name.deserialize_aws_json_1_1(
                data["managedAgentName"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedAgentStateChange.managed_agent_name required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ManagedAgentStateChange.status required")
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
