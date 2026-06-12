"""Generated from Smithy shape ``com.amazonaws.fsx#SvmEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.dns_name
    import aws_sdk_fsx.types.ontap_endpoint_ip_addresses


class SvmEndpoint(TypedDict):
    dns_name: NotRequired["aws_sdk_fsx.types.dns_name.DNSName"]
    ip_addresses: NotRequired[
        "aws_sdk_fsx.types.ontap_endpoint_ip_addresses.OntapEndpointIpAddresses"
    ]
    """<p>The SVM endpoint's IPv4 addresses.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_fsx.types.ontap_endpoint_ip_addresses.OntapEndpointIpAddresses"
    ]
    """<p>The SVM endpoint's IPv6 addresses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SvmEndpoint) -> dict:
    out: dict = {}
    if "dns_name" in value:
        out["DNSName"] = value["dns_name"]
    if "ip_addresses" in value:
        import aws_sdk_fsx.types.ontap_endpoint_ip_addresses

        out["IpAddresses"] = (
            aws_sdk_fsx.types.ontap_endpoint_ip_addresses.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    if "ipv6_addresses" in value:
        import aws_sdk_fsx.types.ontap_endpoint_ip_addresses

        out["Ipv6Addresses"] = (
            aws_sdk_fsx.types.ontap_endpoint_ip_addresses.serialize_aws_json_1_1(
                value["ipv6_addresses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SvmEndpoint:
    out: SvmEndpoint = {}  # type: ignore[typeddict-item]
    if "DNSName" in data:
        out["dns_name"] = data["DNSName"]
    if "IpAddresses" in data:
        import aws_sdk_fsx.types.ontap_endpoint_ip_addresses

        out["ip_addresses"] = (
            aws_sdk_fsx.types.ontap_endpoint_ip_addresses.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    if "Ipv6Addresses" in data:
        import aws_sdk_fsx.types.ontap_endpoint_ip_addresses

        out["ipv6_addresses"] = (
            aws_sdk_fsx.types.ontap_endpoint_ip_addresses.deserialize_aws_json_1_1(
                data["Ipv6Addresses"]
            )
        )
    return out
