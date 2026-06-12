"""Generated from Smithy shape ``com.amazonaws.groundstation#AgentDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_groundstation.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_groundstation.types.agent_cpu_cores_list
    import aws_sdk_groundstation.types.component_version_list
    import aws_sdk_groundstation.types.instance_id
    import aws_sdk_groundstation.types.instance_type
    import aws_sdk_groundstation.types.version_string

class AgentDetails(TypedDict):
    agent_version: "aws_sdk_groundstation.types.version_string.VersionString"
    """<p>Current agent version.</p>"""
    instance_id: "aws_sdk_groundstation.types.instance_id.InstanceId"
    """<p>ID of EC2 instance agent is running on.</p>"""
    instance_type: "aws_sdk_groundstation.types.instance_type.InstanceType"
    """<p>Type of EC2 instance agent is running on.</p>"""
    reserved_cpu_cores: NotRequired["aws_sdk_groundstation.types.agent_cpu_cores_list.AgentCpuCoresList"]
    """<note> <p>This field should not be used. Use agentCpuCores instead.</p> </note> <p>List of CPU cores reserved for processes other than the agent running on the EC2 instance.</p>"""
    agent_cpu_cores: NotRequired["aws_sdk_groundstation.types.agent_cpu_cores_list.AgentCpuCoresList"]
    """<p>List of CPU cores reserved for the agent.</p>"""
    component_versions: "aws_sdk_groundstation.types.component_version_list.ComponentVersionList"
    """<p>List of versions being used by agent components.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AgentDetails) -> dict:
    out: dict = {}
    out["agentVersion"] = value["agent_version"]
    out["instanceId"] = value["instance_id"]
    out["instanceType"] = value["instance_type"]
    if "reserved_cpu_cores" in value:
        import aws_sdk_groundstation.types.agent_cpu_cores_list
        out["reservedCpuCores"] = aws_sdk_groundstation.types.agent_cpu_cores_list.serialize_json(value["reserved_cpu_cores"])
    if "agent_cpu_cores" in value:
        import aws_sdk_groundstation.types.agent_cpu_cores_list
        out["agentCpuCores"] = aws_sdk_groundstation.types.agent_cpu_cores_list.serialize_json(value["agent_cpu_cores"])
    import aws_sdk_groundstation.types.component_version_list
    out["componentVersions"] = aws_sdk_groundstation.types.component_version_list.serialize_json(value["component_versions"])
    return out


def deserialize_json(data: dict) -> AgentDetails:
    out: AgentDetails = {}  # type: ignore[typeddict-item]
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentDetails.agent_version required")
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("AgentDetails.instance_id required")
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("AgentDetails.instance_type required")
    if "reservedCpuCores" in data:
        import aws_sdk_groundstation.types.agent_cpu_cores_list
        out["reserved_cpu_cores"] = aws_sdk_groundstation.types.agent_cpu_cores_list.deserialize_json(data["reservedCpuCores"])
    if "agentCpuCores" in data:
        import aws_sdk_groundstation.types.agent_cpu_cores_list
        out["agent_cpu_cores"] = aws_sdk_groundstation.types.agent_cpu_cores_list.deserialize_json(data["agentCpuCores"])
    if "componentVersions" in data:
        import aws_sdk_groundstation.types.component_version_list
        out["component_versions"] = aws_sdk_groundstation.types.component_version_list.deserialize_json(data["componentVersions"])
    else:
        raise DeserializationError("AgentDetails.component_versions required")
    return out