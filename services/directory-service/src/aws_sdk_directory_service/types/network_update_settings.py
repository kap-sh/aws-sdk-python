"""Generated from Smithy shape ``com.amazonaws.directoryservice#NetworkUpdateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.dns_ipv6_addrs
    import aws_sdk_directory_service.types.network_type


class NetworkUpdateSettings(TypedDict, closed=True):
    network_type: NotRequired[
        "aws_sdk_directory_service.types.network_type.NetworkType"
    ]
    """<p>The target network type for the directory update.</p>"""
    customer_dns_ips_v6: NotRequired[
        "aws_sdk_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>IPv6 addresses of DNS servers or domain controllers in the self-managed directory. Required only when updating an AD Connector directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkUpdateSettings) -> dict:
    out: dict = {}
    if "network_type" in value:
        import aws_sdk_directory_service.types.network_type

        out["NetworkType"] = (
            aws_sdk_directory_service.types.network_type.serialize_aws_json_1_1(
                value["network_type"]
            )
        )
    if "customer_dns_ips_v6" in value:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["CustomerDnsIpsV6"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["customer_dns_ips_v6"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkUpdateSettings:
    out: NetworkUpdateSettings = {}  # type: ignore[typeddict-item]
    if "NetworkType" in data:
        import aws_sdk_directory_service.types.network_type

        out["network_type"] = (
            aws_sdk_directory_service.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    if "CustomerDnsIpsV6" in data:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["customer_dns_ips_v6"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["CustomerDnsIpsV6"]
            )
        )
    return out
