"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VpcInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_string
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.network_interface_type


class VpcInterfaceRequest(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name for the VPC interface. This name must be unique within the flow. </p>"""
    network_interface_type: NotRequired[
        "capo_mediaconnect.types.network_interface_type.NetworkInterfaceType"
    ]
    """<p>The type of network interface. </p>"""
    role_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service. </p>"""
    security_group_ids: NotRequired[
        "capo_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p>A virtual firewall to control inbound and outbound traffic. </p>"""
    subnet_id: NotRequired["str"]
    """<p> The subnet IDs that you want to use for your VPC interface. A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow. </p>"""
    vpc_interface_tags: NotRequired[
        "capo_mediaconnect.types.__map_of_string.__mapOfString"
    ]
    """<p> The key-value pairs that can be used to tag and organize the VPC network interface. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInterfaceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "network_interface_type" in value:
        import capo_mediaconnect.types.network_interface_type

        out["networkInterfaceType"] = (
            capo_mediaconnect.types.network_interface_type.serialize_json(
                value["network_interface_type"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "security_group_ids" in value:
        import capo_mediaconnect.types.__list_of_string

        out["securityGroupIds"] = (
            capo_mediaconnect.types.__list_of_string.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "vpc_interface_tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["vpcInterfaceTags"] = (
            capo_mediaconnect.types.__map_of_string.serialize_json(
                value["vpc_interface_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcInterfaceRequest:
    out: VpcInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "networkInterfaceType" in data:
        import capo_mediaconnect.types.network_interface_type

        out["network_interface_type"] = (
            capo_mediaconnect.types.network_interface_type.deserialize_json(
                data["networkInterfaceType"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "securityGroupIds" in data:
        import capo_mediaconnect.types.__list_of_string

        out["security_group_ids"] = (
            capo_mediaconnect.types.__list_of_string.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "vpcInterfaceTags" in data:
        import capo_mediaconnect.types.__map_of_string

        out["vpc_interface_tags"] = (
            capo_mediaconnect.types.__map_of_string.deserialize_json(
                data["vpcInterfaceTags"]
            )
        )
    return out
