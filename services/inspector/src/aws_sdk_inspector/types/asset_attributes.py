"""Generated from Smithy shape ``com.amazonaws.inspector#AssetAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_id
    import aws_sdk_inspector.types.ami_id
    import aws_sdk_inspector.types.auto_scaling_group
    import aws_sdk_inspector.types.hostname
    import aws_sdk_inspector.types.ipv4_address_list
    import aws_sdk_inspector.types.network_interfaces
    import aws_sdk_inspector.types.numeric_version
    import aws_sdk_inspector.types.tags


class AssetAttributes(TypedDict):
    schema_version: "aws_sdk_inspector.types.numeric_version.NumericVersion"
    """<p>The schema version of this data type.</p>"""
    agent_id: NotRequired["aws_sdk_inspector.types.agent_id.AgentId"]
    """<p>The ID of the agent that is installed on the EC2 instance where the finding is generated.</p>"""
    auto_scaling_group: NotRequired[
        "aws_sdk_inspector.types.auto_scaling_group.AutoScalingGroup"
    ]
    """<p>The Auto Scaling group of the EC2 instance where the finding is generated.</p>"""
    ami_id: NotRequired["aws_sdk_inspector.types.ami_id.AmiId"]
    """<p>The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where the finding is generated.</p>"""
    hostname: NotRequired["aws_sdk_inspector.types.hostname.Hostname"]
    """<p>The hostname of the EC2 instance where the finding is generated.</p>"""
    ipv4_addresses: NotRequired[
        "aws_sdk_inspector.types.ipv4_address_list.Ipv4AddressList"
    ]
    """<p>The list of IP v4 addresses of the EC2 instance where the finding is generated.</p>"""
    tags: NotRequired["aws_sdk_inspector.types.tags.Tags"]
    """<p>The tags related to the EC2 instance where the finding is generated.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_inspector.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>An array of the network interfaces interacting with the EC2 instance where the finding is generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetAttributes) -> dict:
    out: dict = {}
    out["schemaVersion"] = value.get("schema_version", 0)
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "auto_scaling_group" in value:
        out["autoScalingGroup"] = value["auto_scaling_group"]
    if "ami_id" in value:
        out["amiId"] = value["ami_id"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "ipv4_addresses" in value:
        import aws_sdk_inspector.types.ipv4_address_list

        out["ipv4Addresses"] = (
            aws_sdk_inspector.types.ipv4_address_list.serialize_aws_json_1_1(
                value["ipv4_addresses"]
            )
        )
    if "tags" in value:
        import aws_sdk_inspector.types.tags

        out["tags"] = aws_sdk_inspector.types.tags.serialize_aws_json_1_1(value["tags"])
    if "network_interfaces" in value:
        import aws_sdk_inspector.types.network_interfaces

        out["networkInterfaces"] = (
            aws_sdk_inspector.types.network_interfaces.serialize_aws_json_1_1(
                value["network_interfaces"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetAttributes:
    out: AssetAttributes = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = 0
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    if "autoScalingGroup" in data:
        out["auto_scaling_group"] = data["autoScalingGroup"]
    if "amiId" in data:
        out["ami_id"] = data["amiId"]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "ipv4Addresses" in data:
        import aws_sdk_inspector.types.ipv4_address_list

        out["ipv4_addresses"] = (
            aws_sdk_inspector.types.ipv4_address_list.deserialize_aws_json_1_1(
                data["ipv4Addresses"]
            )
        )
    if "tags" in data:
        import aws_sdk_inspector.types.tags

        out["tags"] = aws_sdk_inspector.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "networkInterfaces" in data:
        import aws_sdk_inspector.types.network_interfaces

        out["network_interfaces"] = (
            aws_sdk_inspector.types.network_interfaces.deserialize_aws_json_1_1(
                data["networkInterfaces"]
            )
        )
    return out
