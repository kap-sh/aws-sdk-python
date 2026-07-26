"""Generated from Smithy shape ``com.amazonaws.directconnect#NewTransitVirtualInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.amazon_address
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.bgp_auth_key
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.enable_site_link
    import capo_direct_connect.types.long_asn
    import capo_direct_connect.types.mtu
    import capo_direct_connect.types.tag_list
    import capo_direct_connect.types.virtual_interface_name
    import capo_direct_connect.types.vlan


class NewTransitVirtualInterface(TypedDict, closed=True):
    virtual_interface_name: NotRequired[
        "capo_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    ]
    """<p>The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).</p>"""
    vlan: "capo_direct_connect.types.vlan.VLAN"
    """<p>The ID of the VLAN.</p>"""
    asn: "capo_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    asn_long: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for a new transit virtual interface.The valid range is from 1 to 4294967294 for BGP configuration.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    mtu: NotRequired["capo_direct_connect.types.mtu.MTU"]
    """<p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.</p>"""
    auth_key: NotRequired["capo_direct_connect.types.bgp_auth_key.BGPAuthKey"]
    """<p>The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.</p>"""
    amazon_address: NotRequired[
        "capo_direct_connect.types.amazon_address.AmazonAddress"
    ]
    """<p>The IP address assigned to the Amazon interface.</p>"""
    customer_address: NotRequired[
        "capo_direct_connect.types.customer_address.CustomerAddress"
    ]
    """<p>The IP address assigned to the customer interface.</p>"""
    address_family: NotRequired[
        "capo_direct_connect.types.address_family.AddressFamily"
    ]
    """<p>The address family for the BGP peer.</p>"""
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the transitive virtual interface.</p>"""
    enable_site_link: NotRequired[
        "capo_direct_connect.types.enable_site_link.EnableSiteLink"
    ]
    """<p>Indicates whether to enable or disable SiteLink.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NewTransitVirtualInterface) -> dict:
    out: dict = {}
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    out["vlan"] = value.get("vlan", 0)
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    if "auth_key" in value:
        out["authKey"] = value["auth_key"]
    if "amazon_address" in value:
        out["amazonAddress"] = value["amazon_address"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = (
            capo_direct_connect.types.address_family.serialize_aws_json_1_1(
                value["address_family"]
            )
        )
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "enable_site_link" in value:
        out["enableSiteLink"] = value["enable_site_link"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NewTransitVirtualInterface:
    out: NewTransitVirtualInterface = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceName" in data:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    if "vlan" in data:
        out["vlan"] = data["vlan"]
    else:
        out["vlan"] = 0
    if "asn" in data:
        out["asn"] = data["asn"]
    else:
        out["asn"] = 0
    if "asnLong" in data:
        out["asn_long"] = data["asnLong"]
    if "mtu" in data:
        out["mtu"] = data["mtu"]
    if "authKey" in data:
        out["auth_key"] = data["authKey"]
    if "amazonAddress" in data:
        out["amazon_address"] = data["amazonAddress"]
    if "customerAddress" in data:
        out["customer_address"] = data["customerAddress"]
    if "addressFamily" in data:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_aws_json_1_1(
                data["addressFamily"]
            )
        )
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if "tags" in data:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "enableSiteLink" in data:
        out["enable_site_link"] = data["enableSiteLink"]
    return out
