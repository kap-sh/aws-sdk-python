"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfaceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_network_interface_attachment
    import aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_list
    import aws_sdk_securityhub.types.aws_ec2_network_interface_private_ip_address_list
    import aws_sdk_securityhub.types.aws_ec2_network_interface_security_group_list
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2NetworkInterfaceDetails(TypedDict, closed=True):
    attachment: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_network_interface_attachment.AwsEc2NetworkInterfaceAttachment"
    ]
    """<p>The network interface attachment.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the network interface.</p>"""
    security_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_network_interface_security_group_list.AwsEc2NetworkInterfaceSecurityGroupList"
    ]
    """<p>Security groups for the network interface.</p>"""
    source_dest_check: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether traffic to or from the instance is validated.</p>"""
    ip_v6_addresses: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_list.AwsEc2NetworkInterfaceIpV6AddressList"
    ]
    """<p>The IPv6 addresses associated with the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_network_interface_private_ip_address_list.AwsEc2NetworkInterfacePrivateIpAddressList"
    ]
    """<p>The private IPv4 addresses associated with the network interface.</p>"""
    public_dns_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The public DNS name of the network interface.</p>"""
    public_ip: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The address of the Elastic IP address bound to the network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfaceDetails) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_attachment

        out["Attachment"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_attachment.serialize_json(
                value["attachment"]
            )
        )
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "security_groups" in value:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_security_group_list

        out["SecurityGroups"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_security_group_list.serialize_json(
                value["security_groups"]
            )
        )
    if "source_dest_check" in value:
        out["SourceDestCheck"] = value["source_dest_check"]
    if "ip_v6_addresses" in value:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_list

        out["IpV6Addresses"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_list.serialize_json(
                value["ip_v6_addresses"]
            )
        )
    if "private_ip_addresses" in value:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_private_ip_address_list

        out["PrivateIpAddresses"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_private_ip_address_list.serialize_json(
                value["private_ip_addresses"]
            )
        )
    if "public_dns_name" in value:
        out["PublicDnsName"] = value["public_dns_name"]
    if "public_ip" in value:
        out["PublicIp"] = value["public_ip"]
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkInterfaceDetails:
    out: AwsEc2NetworkInterfaceDetails = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_attachment

        out["attachment"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_attachment.deserialize_json(
                data["Attachment"]
            )
        )
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if "SecurityGroups" in data:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_security_group_list

        out["security_groups"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_security_group_list.deserialize_json(
                data["SecurityGroups"]
            )
        )
    if "SourceDestCheck" in data:
        out["source_dest_check"] = data["SourceDestCheck"]
    if "IpV6Addresses" in data:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_list

        out["ip_v6_addresses"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_list.deserialize_json(
                data["IpV6Addresses"]
            )
        )
    if "PrivateIpAddresses" in data:
        import aws_sdk_securityhub.types.aws_ec2_network_interface_private_ip_address_list

        out["private_ip_addresses"] = (
            aws_sdk_securityhub.types.aws_ec2_network_interface_private_ip_address_list.deserialize_json(
                data["PrivateIpAddresses"]
            )
        )
    if "PublicDnsName" in data:
        out["public_dns_name"] = data["PublicDnsName"]
    if "PublicIp" in data:
        out["public_ip"] = data["PublicIp"]
    return out
