"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2EipDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2EipDetails(TypedDict):
    instance_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the EC2 instance.</p>"""
    public_ip: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A public IP address that is associated with the EC2 instance.</p>"""
    allocation_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier that Amazon Web Services assigns to represent the allocation of the Elastic IP address for use with Amazon VPC.</p>"""
    association_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier that represents the association of the Elastic IP address with an EC2 instance.</p>"""
    domain: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The domain in which to allocate the address.</p> <p>If the address is for use with EC2 instances in a VPC, then <code>Domain</code> is <code>vpc</code>. Otherwise, <code>Domain</code> is <code>standard</code>. </p>"""
    public_ipv4_pool: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of an IP address pool. This parameter allows Amazon EC2 to select an IP address from the address pool.</p>"""
    network_border_group: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the location from which the Elastic IP address is advertised.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the network interface.</p>"""
    network_interface_owner_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account ID of the owner of the network interface.</p>"""
    private_ip_address: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The private IP address that is associated with the Elastic IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2EipDetails) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "public_ip" in value:
        out["PublicIp"] = value["public_ip"]
    if "allocation_id" in value:
        out["AllocationId"] = value["allocation_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "public_ipv4_pool" in value:
        out["PublicIpv4Pool"] = value["public_ipv4_pool"]
    if "network_border_group" in value:
        out["NetworkBorderGroup"] = value["network_border_group"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "network_interface_owner_id" in value:
        out["NetworkInterfaceOwnerId"] = value["network_interface_owner_id"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    return out


def deserialize_json(data: dict) -> AwsEc2EipDetails:
    out: AwsEc2EipDetails = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "PublicIp" in data:
        out["public_ip"] = data["PublicIp"]
    if "AllocationId" in data:
        out["allocation_id"] = data["AllocationId"]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "PublicIpv4Pool" in data:
        out["public_ipv4_pool"] = data["PublicIpv4Pool"]
    if "NetworkBorderGroup" in data:
        out["network_border_group"] = data["NetworkBorderGroup"]
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if "NetworkInterfaceOwnerId" in data:
        out["network_interface_owner_id"] = data["NetworkInterfaceOwnerId"]
    if "PrivateIpAddress" in data:
        out["private_ip_address"] = data["PrivateIpAddress"]
    return out
