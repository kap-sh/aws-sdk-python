"""Generated from Smithy shape ``com.amazonaws.vpclattice#DnsResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.domain_name
    import aws_sdk_vpc_lattice.types.resource_configuration_ip_address_type


class DnsResource(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_vpc_lattice.types.domain_name.DomainName"]
    """<p>The domain name of the resource.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_ip_address_type.ResourceConfigurationIpAddressType"
    ]
    """<p>The type of IP address. Dualstack is currently not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsResource) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    return out


def deserialize_json(data: dict) -> DnsResource:
    out: DnsResource = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "ipAddressType" in data:
        out["ip_address_type"] = data["ipAddressType"]
    return out
