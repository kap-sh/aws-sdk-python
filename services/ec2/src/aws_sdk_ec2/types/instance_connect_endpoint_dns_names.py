"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceConnectEndpointDnsNames``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceConnectEndpointDnsNames(TypedDict):
    dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name of the EC2 Instance Connect Endpoint.</p>"""
    fips_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Federal Information Processing Standards (FIPS) compliant DNS name of the EC2 Instance Connect Endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceConnectEndpointDnsNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dns_name" in value:
        pairs.append((f"{prefix}.DnsName", str(value["dns_name"])))
    if "fips_dns_name" in value:
        pairs.append((f"{prefix}.FipsDnsName", str(value["fips_dns_name"])))


def deserialize_ec2_query(el: Element) -> InstanceConnectEndpointDnsNames:
    out: InstanceConnectEndpointDnsNames = {}  # type: ignore[typeddict-item]
    child_dns_name = el.find("DnsName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    child_fips_dns_name = el.find("FipsDnsName")
    if child_fips_dns_name is not None:
        out["fips_dns_name"] = str(child_fips_dns_name.text or "")
    return out
