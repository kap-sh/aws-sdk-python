"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.dns_name
    import capo_fsx.types.ontap_endpoint_ip_addresses


class FileSystemEndpoint(TypedDict, closed=True):
    dns_name: NotRequired["capo_fsx.types.dns_name.DNSName"]
    ip_addresses: NotRequired[
        "capo_fsx.types.ontap_endpoint_ip_addresses.OntapEndpointIpAddresses"
    ]
    """<p>The IPv4 addresses of the file system endpoint.</p>"""
    ipv6_addresses: NotRequired[
        "capo_fsx.types.ontap_endpoint_ip_addresses.OntapEndpointIpAddresses"
    ]
    """<p>The IPv6 addresses of the file system endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemEndpoint) -> dict:
    out: dict = {}
    if "dns_name" in value:
        out["DNSName"] = value["dns_name"]
    if "ip_addresses" in value:
        import capo_fsx.types.ontap_endpoint_ip_addresses

        out["IpAddresses"] = (
            capo_fsx.types.ontap_endpoint_ip_addresses.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    if "ipv6_addresses" in value:
        import capo_fsx.types.ontap_endpoint_ip_addresses

        out["Ipv6Addresses"] = (
            capo_fsx.types.ontap_endpoint_ip_addresses.serialize_aws_json_1_1(
                value["ipv6_addresses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemEndpoint:
    out: FileSystemEndpoint = {}  # type: ignore[typeddict-item]
    if "DNSName" in data:
        out["dns_name"] = data["DNSName"]
    if "IpAddresses" in data:
        import capo_fsx.types.ontap_endpoint_ip_addresses

        out["ip_addresses"] = (
            capo_fsx.types.ontap_endpoint_ip_addresses.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    if "Ipv6Addresses" in data:
        import capo_fsx.types.ontap_endpoint_ip_addresses

        out["ipv6_addresses"] = (
            capo_fsx.types.ontap_endpoint_ip_addresses.deserialize_aws_json_1_1(
                data["Ipv6Addresses"]
            )
        )
    return out
