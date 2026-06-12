"""Generated from Smithy shape ``com.amazonaws.inspector#NetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector.types.ipv6_addresses
    import aws_sdk_inspector.types.private_ip_addresses
    import aws_sdk_inspector.types.security_groups
    import aws_sdk_inspector.types.text


class NetworkInterface(TypedDict):
    network_interface_id: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The ID of the network interface.</p>"""
    subnet_id: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The ID of a subnet associated with the network interface.</p>"""
    vpc_id: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The ID of a VPC associated with the network interface.</p>"""
    private_dns_name: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The name of a private DNS associated with the network interface.</p>"""
    private_ip_address: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The private IP address associated with the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_inspector.types.private_ip_addresses.PrivateIpAddresses"
    ]
    """<p>A list of the private IP addresses associated with the network interface. Includes the privateDnsName and privateIpAddress.</p>"""
    public_dns_name: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The name of a public DNS associated with the network interface.</p>"""
    public_ip: NotRequired["aws_sdk_inspector.types.text.Text"]
    """<p>The public IP address from which the network interface is reachable.</p>"""
    ipv6_addresses: NotRequired["aws_sdk_inspector.types.ipv6_addresses.Ipv6Addresses"]
    """<p>The IP addresses associated with the network interface.</p>"""
    security_groups: NotRequired[
        "aws_sdk_inspector.types.security_groups.SecurityGroups"
    ]
    """<p>A list of the security groups associated with the network interface. Includes the groupId and groupName.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterface) -> dict:
    out: dict = {}
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "private_dns_name" in value:
        out["privateDnsName"] = value["private_dns_name"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    if "private_ip_addresses" in value:
        import aws_sdk_inspector.types.private_ip_addresses

        out["privateIpAddresses"] = (
            aws_sdk_inspector.types.private_ip_addresses.serialize_aws_json_1_1(
                value["private_ip_addresses"]
            )
        )
    if "public_dns_name" in value:
        out["publicDnsName"] = value["public_dns_name"]
    if "public_ip" in value:
        out["publicIp"] = value["public_ip"]
    if "ipv6_addresses" in value:
        import aws_sdk_inspector.types.ipv6_addresses

        out["ipv6Addresses"] = (
            aws_sdk_inspector.types.ipv6_addresses.serialize_aws_json_1_1(
                value["ipv6_addresses"]
            )
        )
    if "security_groups" in value:
        import aws_sdk_inspector.types.security_groups

        out["securityGroups"] = (
            aws_sdk_inspector.types.security_groups.serialize_aws_json_1_1(
                value["security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "networkInterfaceId" in data:
        out["network_interface_id"] = data["networkInterfaceId"]
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "privateDnsName" in data:
        out["private_dns_name"] = data["privateDnsName"]
    if "privateIpAddress" in data:
        out["private_ip_address"] = data["privateIpAddress"]
    if "privateIpAddresses" in data:
        import aws_sdk_inspector.types.private_ip_addresses

        out["private_ip_addresses"] = (
            aws_sdk_inspector.types.private_ip_addresses.deserialize_aws_json_1_1(
                data["privateIpAddresses"]
            )
        )
    if "publicDnsName" in data:
        out["public_dns_name"] = data["publicDnsName"]
    if "publicIp" in data:
        out["public_ip"] = data["publicIp"]
    if "ipv6Addresses" in data:
        import aws_sdk_inspector.types.ipv6_addresses

        out["ipv6_addresses"] = (
            aws_sdk_inspector.types.ipv6_addresses.deserialize_aws_json_1_1(
                data["ipv6Addresses"]
            )
        )
    if "securityGroups" in data:
        import aws_sdk_inspector.types.security_groups

        out["security_groups"] = (
            aws_sdk_inspector.types.security_groups.deserialize_aws_json_1_1(
                data["securityGroups"]
            )
        )
    return out
