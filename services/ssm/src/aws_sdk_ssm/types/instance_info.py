"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.agent_type
    import aws_sdk_ssm.types.agent_version
    import aws_sdk_ssm.types.computer_name
    import aws_sdk_ssm.types.instance_status
    import aws_sdk_ssm.types.ip_address
    import aws_sdk_ssm.types.managed_status
    import aws_sdk_ssm.types.platform_name
    import aws_sdk_ssm.types.platform_type
    import aws_sdk_ssm.types.platform_version
    import aws_sdk_ssm.types.resource_type


class InstanceInfo(TypedDict):
    agent_type: NotRequired["aws_sdk_ssm.types.agent_type.AgentType"]
    """<p>The type of agent installed on the node.</p>"""
    agent_version: NotRequired["aws_sdk_ssm.types.agent_version.AgentVersion"]
    """<p>The version number of the agent installed on the node.</p>"""
    computer_name: NotRequired["aws_sdk_ssm.types.computer_name.ComputerName"]
    """<p>The fully qualified host name of the managed node.</p>"""
    instance_status: NotRequired["aws_sdk_ssm.types.instance_status.InstanceStatus"]
    """<p>The current status of the managed node.</p>"""
    ip_address: NotRequired["aws_sdk_ssm.types.ip_address.IPAddress"]
    """<p>The IP address of the managed node.</p>"""
    managed_status: NotRequired["aws_sdk_ssm.types.managed_status.ManagedStatus"]
    """<p>Indicates whether the node is managed by Systems Manager.</p>"""
    platform_type: NotRequired["aws_sdk_ssm.types.platform_type.PlatformType"]
    """<p>The operating system platform type of the managed node.</p>"""
    platform_name: NotRequired["aws_sdk_ssm.types.platform_name.PlatformName"]
    """<p>The name of the operating system platform running on your managed node.</p>"""
    platform_version: NotRequired["aws_sdk_ssm.types.platform_version.PlatformVersion"]
    """<p>The version of the OS platform running on your managed node. </p>"""
    resource_type: NotRequired["aws_sdk_ssm.types.resource_type.ResourceType"]
    """<p>The type of instance, either an EC2 instance or another supported machine type in a hybrid fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInfo) -> dict:
    out: dict = {}
    if "agent_type" in value:
        out["AgentType"] = value["agent_type"]
    if "agent_version" in value:
        out["AgentVersion"] = value["agent_version"]
    if "computer_name" in value:
        out["ComputerName"] = value["computer_name"]
    if "instance_status" in value:
        out["InstanceStatus"] = value["instance_status"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "managed_status" in value:
        import aws_sdk_ssm.types.managed_status

        out["ManagedStatus"] = aws_sdk_ssm.types.managed_status.serialize_aws_json_1_1(
            value["managed_status"]
        )
    if "platform_type" in value:
        import aws_sdk_ssm.types.platform_type

        out["PlatformType"] = aws_sdk_ssm.types.platform_type.serialize_aws_json_1_1(
            value["platform_type"]
        )
    if "platform_name" in value:
        out["PlatformName"] = value["platform_name"]
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "resource_type" in value:
        import aws_sdk_ssm.types.resource_type

        out["ResourceType"] = aws_sdk_ssm.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInfo:
    out: InstanceInfo = {}  # type: ignore[typeddict-item]
    if "AgentType" in data:
        out["agent_type"] = data["AgentType"]
    if "AgentVersion" in data:
        out["agent_version"] = data["AgentVersion"]
    if "ComputerName" in data:
        out["computer_name"] = data["ComputerName"]
    if "InstanceStatus" in data:
        out["instance_status"] = data["InstanceStatus"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "ManagedStatus" in data:
        import aws_sdk_ssm.types.managed_status

        out["managed_status"] = (
            aws_sdk_ssm.types.managed_status.deserialize_aws_json_1_1(
                data["ManagedStatus"]
            )
        )
    if "PlatformType" in data:
        import aws_sdk_ssm.types.platform_type

        out["platform_type"] = aws_sdk_ssm.types.platform_type.deserialize_aws_json_1_1(
            data["PlatformType"]
        )
    if "PlatformName" in data:
        out["platform_name"] = data["PlatformName"]
    if "PlatformVersion" in data:
        out["platform_version"] = data["PlatformVersion"]
    if "ResourceType" in data:
        import aws_sdk_ssm.types.resource_type

        out["resource_type"] = aws_sdk_ssm.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    return out
