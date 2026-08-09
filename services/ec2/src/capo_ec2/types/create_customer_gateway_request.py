"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCustomerGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.gateway_type
    import capo_ec2.types.integer
    import capo_ec2.types.long
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateCustomerGatewayRequest(TypedDict, closed=True):
    bgp_asn: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>For customer gateway devices that support BGP, specify the device's ASN. You must specify either <code>BgpAsn</code> or <code>BgpAsnExtended</code> when creating the customer gateway. If the ASN is larger than <code>2,147,483,647</code>, you must use <code>BgpAsnExtended</code>.</p> <p>Default: 65000</p> <p>Valid values: <code>1</code> to <code>2,147,483,647</code> </p>"""
    public_ip: NotRequired["capo_ec2.types.string.String"]
    """<p> <i>This member has been deprecated.</i> The Internet-routable IP address for the customer gateway's outside interface. The address must be static.</p>"""
    certificate_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the customer gateway certificate.</p>"""
    type: NotRequired["capo_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection that this customer gateway supports (<code>ipsec.1</code>).</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the customer gateway.</p>"""
    device_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A name for the customer gateway device.</p> <p>Length Constraints: Up to 255 characters.</p>"""
    ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address for the customer gateway device's outside interface. The address must be static. If <code>OutsideIpAddressType</code> in your VPN connection options is set to <code>PrivateIpv4</code>, you can use an RFC6598 or RFC1918 private IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>Ipv6</code>, you can use an IPv6 address. </p>"""
    bgp_asn_extended: NotRequired["capo_ec2.types.long.Long"]
    """<p>For customer gateway devices that support BGP, specify the device's ASN. You must specify either <code>BgpAsn</code> or <code>BgpAsnExtended</code> when creating the customer gateway. If the ASN is larger than <code>2,147,483,647</code>, you must use <code>BgpAsnExtended</code>.</p> <p>Valid values: <code>2,147,483,648</code> to <code>4,294,967,295</code> </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCustomerGatewayRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "bgp_asn" in value:
        pairs.append((f"{key_prefix}BgpAsn", str(value["bgp_asn"])))
    if "public_ip" in value:
        pairs.append((f"{key_prefix}PublicIp", str(value["public_ip"])))
    if "certificate_arn" in value:
        pairs.append((f"{key_prefix}CertificateArn", str(value["certificate_arn"])))
    if "type" in value:
        import capo_ec2.types.gateway_type

        capo_ec2.types.gateway_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "device_name" in value:
        pairs.append((f"{key_prefix}DeviceName", str(value["device_name"])))
    if "ip_address" in value:
        pairs.append((f"{key_prefix}IpAddress", str(value["ip_address"])))
    if "bgp_asn_extended" in value:
        pairs.append((f"{key_prefix}BgpAsnExtended", str(value["bgp_asn_extended"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateCustomerGatewayRequest:
    out: CreateCustomerGatewayRequest = {}  # type: ignore[typeddict-item]
    child_bgp_asn = el.find("BgpAsn")
    if child_bgp_asn is not None:
        out["bgp_asn"] = int(child_bgp_asn.text or "")
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_ec2.types.gateway_type

        out["type"] = capo_ec2.types.gateway_type.deserialize_ec2_query(child_type)
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_ip_address = el.find("IpAddress")
    if child_ip_address is not None:
        out["ip_address"] = str(child_ip_address.text or "")
    child_bgp_asn_extended = el.find("BgpAsnExtended")
    if child_bgp_asn_extended is not None:
        out["bgp_asn_extended"] = int(child_bgp_asn_extended.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
