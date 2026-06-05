"""Generated from Smithy shape ``com.amazonaws.ec2#CustomerGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CustomerGateway(TypedDict):
    certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the customer gateway certificate.</p>"""
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of customer gateway device.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the customer gateway.</p>"""
    bgp_asn_extended: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN).</p> <p>Valid values: <code>2,147,483,648</code> to <code>4,294,967,295</code> </p>"""
    customer_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the customer gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the customer gateway (<code>pending | available | deleting | deleted</code>).</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of VPN connection the customer gateway supports (<code>ipsec.1</code>).</p>"""
    ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The IP address for the customer gateway device's outside interface. The address must be static. If <code>OutsideIpAddressType</code> in your VPN connection options is set to <code>PrivateIpv4</code>, you can use an RFC6598 or RFC1918 private IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>PublicIpv4</code>, you can use a public IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>Ipv6</code>, you can use a public IPv6 address. </p>"""
    bgp_asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN).</p> <p>Valid values: <code>1</code> to <code>2,147,483,647</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CustomerGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificate_arn" in value:
        pairs.append((f"{prefix}.CertificateArn", str(value["certificate_arn"])))
    if "device_name" in value:
        pairs.append((f"{prefix}.DeviceName", str(value["device_name"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "bgp_asn_extended" in value:
        pairs.append((f"{prefix}.BgpAsnExtended", str(value["bgp_asn_extended"])))
    if "customer_gateway_id" in value:
        pairs.append((f"{prefix}.CustomerGatewayId", str(value["customer_gateway_id"])))
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))
    if "ip_address" in value:
        pairs.append((f"{prefix}.IpAddress", str(value["ip_address"])))
    if "bgp_asn" in value:
        pairs.append((f"{prefix}.BgpAsn", str(value["bgp_asn"])))


def deserialize_ec2_query(el: Element) -> CustomerGateway:
    out: CustomerGateway = {}  # type: ignore[typeddict-item]
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_bgp_asn_extended = el.find("BgpAsnExtended")
    if child_bgp_asn_extended is not None:
        out["bgp_asn_extended"] = str(child_bgp_asn_extended.text or "")
    child_customer_gateway_id = el.find("CustomerGatewayId")
    if child_customer_gateway_id is not None:
        out["customer_gateway_id"] = str(child_customer_gateway_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_ip_address = el.find("IpAddress")
    if child_ip_address is not None:
        out["ip_address"] = str(child_ip_address.text or "")
    child_bgp_asn = el.find("BgpAsn")
    if child_bgp_asn is not None:
        out["bgp_asn"] = str(child_bgp_asn.text or "")
    return out
