"""Generated from Smithy shape ``com.amazonaws.inspector#AgentPreview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.agent_health
    import capo_inspector.types.agent_id
    import capo_inspector.types.agent_version
    import capo_inspector.types.auto_scaling_group
    import capo_inspector.types.hostname
    import capo_inspector.types.ipv4_address
    import capo_inspector.types.kernel_version
    import capo_inspector.types.operating_system


class AgentPreview(TypedDict, closed=True):
    hostname: NotRequired["capo_inspector.types.hostname.Hostname"]
    """<p>The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.</p>"""
    agent_id: "capo_inspector.types.agent_id.AgentId"
    """<p>The ID of the EC2 instance where the agent is installed.</p>"""
    auto_scaling_group: NotRequired[
        "capo_inspector.types.auto_scaling_group.AutoScalingGroup"
    ]
    """<p>The Auto Scaling group for the EC2 instance where the agent is installed.</p>"""
    agent_health: NotRequired["capo_inspector.types.agent_health.AgentHealth"]
    """<p>The health status of the Amazon Inspector Agent.</p>"""
    agent_version: NotRequired["capo_inspector.types.agent_version.AgentVersion"]
    """<p>The version of the Amazon Inspector Agent.</p>"""
    operating_system: NotRequired[
        "capo_inspector.types.operating_system.OperatingSystem"
    ]
    """<p>The operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.</p>"""
    kernel_version: NotRequired["capo_inspector.types.kernel_version.KernelVersion"]
    """<p>The kernel version of the operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.</p>"""
    ipv4_address: NotRequired["capo_inspector.types.ipv4_address.Ipv4Address"]
    """<p>The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentPreview) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    out["agentId"] = value["agent_id"]
    if "auto_scaling_group" in value:
        out["autoScalingGroup"] = value["auto_scaling_group"]
    if "agent_health" in value:
        import capo_inspector.types.agent_health

        out["agentHealth"] = capo_inspector.types.agent_health.serialize_aws_json_1_1(
            value["agent_health"]
        )
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "kernel_version" in value:
        out["kernelVersion"] = value["kernel_version"]
    if "ipv4_address" in value:
        out["ipv4Address"] = value["ipv4_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentPreview:
    out: AgentPreview = {}  # type: ignore[typeddict-item]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentPreview.agent_id required")
    if "autoScalingGroup" in data:
        out["auto_scaling_group"] = data["autoScalingGroup"]
    if "agentHealth" in data:
        import capo_inspector.types.agent_health

        out["agent_health"] = (
            capo_inspector.types.agent_health.deserialize_aws_json_1_1(
                data["agentHealth"]
            )
        )
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    if "operatingSystem" in data:
        out["operating_system"] = data["operatingSystem"]
    if "kernelVersion" in data:
        out["kernel_version"] = data["kernelVersion"]
    if "ipv4Address" in data:
        out["ipv4_address"] = data["ipv4Address"]
    return out
