"""Generated from Smithy shape ``com.amazonaws.directconnect#NewPublicVirtualInterfaceAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.address_family
    import aws_sdk_direct_connect.types.amazon_address
    import aws_sdk_direct_connect.types.asn
    import aws_sdk_direct_connect.types.bgp_auth_key
    import aws_sdk_direct_connect.types.customer_address
    import aws_sdk_direct_connect.types.long_asn
    import aws_sdk_direct_connect.types.route_filter_prefix_list
    import aws_sdk_direct_connect.types.tag_list
    import aws_sdk_direct_connect.types.virtual_interface_name
    import aws_sdk_direct_connect.types.vlan


class NewPublicVirtualInterfaceAllocation(TypedDict, closed=True):
    virtual_interface_name: (
        "aws_sdk_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    )
    """<p>The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).</p>"""
    vlan: "aws_sdk_direct_connect.types.vlan.VLAN"
    """<p>The ID of the VLAN.</p>"""
    asn: "aws_sdk_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note> <p>The valid values are 1-2147483646.</p>"""
    asn_long: NotRequired["aws_sdk_direct_connect.types.long_asn.LongAsn"]
    """<p>The ASN when allocating a new public virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    auth_key: NotRequired["aws_sdk_direct_connect.types.bgp_auth_key.BGPAuthKey"]
    """<p>The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.</p>"""
    amazon_address: NotRequired[
        "aws_sdk_direct_connect.types.amazon_address.AmazonAddress"
    ]
    """<p>The IP address assigned to the Amazon interface.</p>"""
    customer_address: NotRequired[
        "aws_sdk_direct_connect.types.customer_address.CustomerAddress"
    ]
    """<p>The IP address assigned to the customer interface.</p>"""
    address_family: NotRequired[
        "aws_sdk_direct_connect.types.address_family.AddressFamily"
    ]
    """<p>The address family for the BGP peer.</p>"""
    route_filter_prefixes: NotRequired[
        "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The routes to be advertised to the Amazon Web Services network in this Region. Applies to public virtual interfaces.</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the public virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NewPublicVirtualInterfaceAllocation) -> dict:
    out: dict = {}
    out["virtualInterfaceName"] = value["virtual_interface_name"]
    out["vlan"] = value.get("vlan", 0)
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "auth_key" in value:
        out["authKey"] = value["auth_key"]
    if "amazon_address" in value:
        out["amazonAddress"] = value["amazon_address"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "address_family" in value:
        import aws_sdk_direct_connect.types.address_family

        out["addressFamily"] = (
            aws_sdk_direct_connect.types.address_family.serialize_aws_json_1_1(
                value["address_family"]
            )
        )
    if "route_filter_prefixes" in value:
        import aws_sdk_direct_connect.types.route_filter_prefix_list

        out["routeFilterPrefixes"] = (
            aws_sdk_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["route_filter_prefixes"]
            )
        )
    if "tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NewPublicVirtualInterfaceAllocation:
    out: NewPublicVirtualInterfaceAllocation = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceName" in data:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    else:
        raise DeserializationError(
            "NewPublicVirtualInterfaceAllocation.virtual_interface_name required"
        )
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
    if "authKey" in data:
        out["auth_key"] = data["authKey"]
    if "amazonAddress" in data:
        out["amazon_address"] = data["amazonAddress"]
    if "customerAddress" in data:
        out["customer_address"] = data["customerAddress"]
    if "addressFamily" in data:
        import aws_sdk_direct_connect.types.address_family

        out["address_family"] = (
            aws_sdk_direct_connect.types.address_family.deserialize_aws_json_1_1(
                data["addressFamily"]
            )
        )
    if "routeFilterPrefixes" in data:
        import aws_sdk_direct_connect.types.route_filter_prefix_list

        out["route_filter_prefixes"] = (
            aws_sdk_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["routeFilterPrefixes"]
            )
        )
    if "tags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
