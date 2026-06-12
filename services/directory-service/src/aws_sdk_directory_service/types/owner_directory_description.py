"""Generated from Smithy shape ``com.amazonaws.directoryservice#OwnerDirectoryDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.customer_id
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.directory_vpc_settings_description
    import aws_sdk_directory_service.types.dns_ip_addrs
    import aws_sdk_directory_service.types.dns_ipv6_addrs
    import aws_sdk_directory_service.types.network_type
    import aws_sdk_directory_service.types.radius_settings
    import aws_sdk_directory_service.types.radius_status


class OwnerDirectoryDescription(TypedDict):
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>Identifier of the Managed Microsoft AD directory in the directory owner account.</p>"""
    account_id: NotRequired["aws_sdk_directory_service.types.customer_id.CustomerId"]
    """<p>Identifier of the directory owner account.</p>"""
    dns_ip_addrs: NotRequired["aws_sdk_directory_service.types.dns_ip_addrs.DnsIpAddrs"]
    """<p>IP address of the directory’s domain controllers.</p>"""
    dns_ipv6_addrs: NotRequired[
        "aws_sdk_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>IPv6 addresses of the directory’s domain controllers.</p>"""
    vpc_settings: NotRequired[
        "aws_sdk_directory_service.types.directory_vpc_settings_description.DirectoryVpcSettingsDescription"
    ]
    """<p>Information about the VPC settings for the directory.</p>"""
    radius_settings: NotRequired[
        "aws_sdk_directory_service.types.radius_settings.RadiusSettings"
    ]
    """<p>Information about the <a>RadiusSettings</a> object server configuration.</p>"""
    radius_status: NotRequired[
        "aws_sdk_directory_service.types.radius_status.RadiusStatus"
    ]
    """<p>The status of the RADIUS server.</p>"""
    network_type: NotRequired[
        "aws_sdk_directory_service.types.network_type.NetworkType"
    ]
    """<p>Network type of the directory in the directory owner account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OwnerDirectoryDescription) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "dns_ip_addrs" in value:
        import aws_sdk_directory_service.types.dns_ip_addrs

        out["DnsIpAddrs"] = (
            aws_sdk_directory_service.types.dns_ip_addrs.serialize_aws_json_1_1(
                value["dns_ip_addrs"]
            )
        )
    if "dns_ipv6_addrs" in value:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["DnsIpv6Addrs"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["dns_ipv6_addrs"]
            )
        )
    if "vpc_settings" in value:
        import aws_sdk_directory_service.types.directory_vpc_settings_description

        out["VpcSettings"] = (
            aws_sdk_directory_service.types.directory_vpc_settings_description.serialize_aws_json_1_1(
                value["vpc_settings"]
            )
        )
    if "radius_settings" in value:
        import aws_sdk_directory_service.types.radius_settings

        out["RadiusSettings"] = (
            aws_sdk_directory_service.types.radius_settings.serialize_aws_json_1_1(
                value["radius_settings"]
            )
        )
    if "radius_status" in value:
        import aws_sdk_directory_service.types.radius_status

        out["RadiusStatus"] = (
            aws_sdk_directory_service.types.radius_status.serialize_aws_json_1_1(
                value["radius_status"]
            )
        )
    if "network_type" in value:
        import aws_sdk_directory_service.types.network_type

        out["NetworkType"] = (
            aws_sdk_directory_service.types.network_type.serialize_aws_json_1_1(
                value["network_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OwnerDirectoryDescription:
    out: OwnerDirectoryDescription = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "DnsIpAddrs" in data:
        import aws_sdk_directory_service.types.dns_ip_addrs

        out["dns_ip_addrs"] = (
            aws_sdk_directory_service.types.dns_ip_addrs.deserialize_aws_json_1_1(
                data["DnsIpAddrs"]
            )
        )
    if "DnsIpv6Addrs" in data:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["dns_ipv6_addrs"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["DnsIpv6Addrs"]
            )
        )
    if "VpcSettings" in data:
        import aws_sdk_directory_service.types.directory_vpc_settings_description

        out["vpc_settings"] = (
            aws_sdk_directory_service.types.directory_vpc_settings_description.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    if "RadiusSettings" in data:
        import aws_sdk_directory_service.types.radius_settings

        out["radius_settings"] = (
            aws_sdk_directory_service.types.radius_settings.deserialize_aws_json_1_1(
                data["RadiusSettings"]
            )
        )
    if "RadiusStatus" in data:
        import aws_sdk_directory_service.types.radius_status

        out["radius_status"] = (
            aws_sdk_directory_service.types.radius_status.deserialize_aws_json_1_1(
                data["RadiusStatus"]
            )
        )
    if "NetworkType" in data:
        import aws_sdk_directory_service.types.network_type

        out["network_type"] = (
            aws_sdk_directory_service.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    return out
