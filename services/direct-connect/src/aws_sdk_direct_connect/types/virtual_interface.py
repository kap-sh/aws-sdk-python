"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.address_family
    import aws_sdk_direct_connect.types.amazon_address
    import aws_sdk_direct_connect.types.asn
    import aws_sdk_direct_connect.types.aws_device_v2
    import aws_sdk_direct_connect.types.aws_logical_device_id
    import aws_sdk_direct_connect.types.bgp_auth_key
    import aws_sdk_direct_connect.types.bgp_peer_list
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.customer_address
    import aws_sdk_direct_connect.types.direct_connect_gateway_id
    import aws_sdk_direct_connect.types.jumbo_frame_capable
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.long_asn
    import aws_sdk_direct_connect.types.mtu
    import aws_sdk_direct_connect.types.owner_account
    import aws_sdk_direct_connect.types.region
    import aws_sdk_direct_connect.types.route_filter_prefix_list
    import aws_sdk_direct_connect.types.router_config
    import aws_sdk_direct_connect.types.site_link_enabled
    import aws_sdk_direct_connect.types.tag_list
    import aws_sdk_direct_connect.types.virtual_gateway_id
    import aws_sdk_direct_connect.types.virtual_interface_id
    import aws_sdk_direct_connect.types.virtual_interface_name
    import aws_sdk_direct_connect.types.virtual_interface_state
    import aws_sdk_direct_connect.types.virtual_interface_type
    import aws_sdk_direct_connect.types.vlan


class VirtualInterface(TypedDict, closed=True):
    owner_account: NotRequired[
        "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the virtual interface.</p>"""
    virtual_interface_id: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    location: NotRequired["aws_sdk_direct_connect.types.location_code.LocationCode"]
    """<p>The location of the connection.</p>"""
    connection_id: NotRequired[
        "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    ]
    """<p>The ID of the connection.</p>"""
    virtual_interface_type: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_type.VirtualInterfaceType"
    ]
    """<p>The type of virtual interface. The possible values are <code>private</code>, <code>public</code> and <code>transit</code>.</p>"""
    virtual_interface_name: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    ]
    """<p>The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).</p>"""
    vlan: "aws_sdk_direct_connect.types.vlan.VLAN"
    """<p>The ID of the VLAN.</p>"""
    asn: "aws_sdk_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    asn_long: NotRequired["aws_sdk_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for the virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    amazon_side_asn: NotRequired["aws_sdk_direct_connect.types.long_asn.LongAsn"]
    """<p>The autonomous system number (AS) for the Amazon side of the connection.</p>"""
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
    virtual_interface_state: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_state.VirtualInterfaceState"
    ]
    """<p>The state of the virtual interface. The following are the possible values:</p> <ul> <li> <p> <code>confirming</code>: The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.</p> </li> <li> <p> <code>verifying</code>: This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.</p> </li> <li> <p> <code>pending</code>: A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.</p> </li> <li> <p> <code>available</code>: A virtual interface that is able to forward traffic.</p> </li> <li> <p> <code>down</code>: A virtual interface that is BGP down.</p> </li> <li> <p> <code>testing</code>: A virtual interface is in this state immediately after calling <a>StartBgpFailoverTest</a> and remains in this state during the duration of the test.</p> </li> <li> <p> <code>deleting</code>: A virtual interface is in this state immediately after calling <a>DeleteVirtualInterface</a> until it can no longer forward traffic.</p> </li> <li> <p> <code>deleted</code>: A virtual interface that cannot forward traffic.</p> </li> <li> <p> <code>rejected</code>: The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the <code>Confirming</code> state is deleted by the virtual interface owner, the virtual interface enters the <code>Rejected</code> state.</p> </li> <li> <p> <code>unknown</code>: The state of the virtual interface is not available.</p> </li> </ul>"""
    customer_router_config: NotRequired[
        "aws_sdk_direct_connect.types.router_config.RouterConfig"
    ]
    """<p>The customer router configuration.</p>"""
    mtu: NotRequired["aws_sdk_direct_connect.types.mtu.MTU"]
    """<p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500</p>"""
    jumbo_frame_capable: NotRequired[
        "aws_sdk_direct_connect.types.jumbo_frame_capable.JumboFrameCapable"
    ]
    """<p>Indicates whether jumbo frames are supported.</p>"""
    virtual_gateway_id: NotRequired[
        "aws_sdk_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway. Applies only to private virtual interfaces.</p>"""
    direct_connect_gateway_id: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    route_filter_prefixes: NotRequired[
        "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The routes to be advertised to the Amazon Web Services network in this Region. Applies to public virtual interfaces.</p>"""
    bgp_peers: NotRequired["aws_sdk_direct_connect.types.bgp_peer_list.BGPPeerList"]
    """<p>The BGP peers configured on this virtual interface.</p>"""
    region: NotRequired["aws_sdk_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region where the virtual interface is located.</p>"""
    aws_device_v2: NotRequired["aws_sdk_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that terminates the physical connection.</p>"""
    aws_logical_device_id: NotRequired[
        "aws_sdk_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the virtual interface.</p>"""
    site_link_enabled: NotRequired[
        "aws_sdk_direct_connect.types.site_link_enabled.SiteLinkEnabled"
    ]
    """<p>Indicates whether SiteLink is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterface) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "location" in value:
        out["location"] = value["location"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "virtual_interface_type" in value:
        out["virtualInterfaceType"] = value["virtual_interface_type"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    out["vlan"] = value.get("vlan", 0)
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "amazon_side_asn" in value:
        out["amazonSideAsn"] = value["amazon_side_asn"]
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
    if "virtual_interface_state" in value:
        import aws_sdk_direct_connect.types.virtual_interface_state

        out["virtualInterfaceState"] = (
            aws_sdk_direct_connect.types.virtual_interface_state.serialize_aws_json_1_1(
                value["virtual_interface_state"]
            )
        )
    if "customer_router_config" in value:
        out["customerRouterConfig"] = value["customer_router_config"]
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "route_filter_prefixes" in value:
        import aws_sdk_direct_connect.types.route_filter_prefix_list

        out["routeFilterPrefixes"] = (
            aws_sdk_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["route_filter_prefixes"]
            )
        )
    if "bgp_peers" in value:
        import aws_sdk_direct_connect.types.bgp_peer_list

        out["bgpPeers"] = (
            aws_sdk_direct_connect.types.bgp_peer_list.serialize_aws_json_1_1(
                value["bgp_peers"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "site_link_enabled" in value:
        out["siteLinkEnabled"] = value["site_link_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VirtualInterface:
    out: VirtualInterface = {}  # type: ignore[typeddict-item]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if "location" in data:
        out["location"] = data["location"]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    if "virtualInterfaceType" in data:
        out["virtual_interface_type"] = data["virtualInterfaceType"]
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
    if "amazonSideAsn" in data:
        out["amazon_side_asn"] = data["amazonSideAsn"]
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
    if "virtualInterfaceState" in data:
        import aws_sdk_direct_connect.types.virtual_interface_state

        out["virtual_interface_state"] = (
            aws_sdk_direct_connect.types.virtual_interface_state.deserialize_aws_json_1_1(
                data["virtualInterfaceState"]
            )
        )
    if "customerRouterConfig" in data:
        out["customer_router_config"] = data["customerRouterConfig"]
    if "mtu" in data:
        out["mtu"] = data["mtu"]
    if "jumboFrameCapable" in data:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if "virtualGatewayId" in data:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if "routeFilterPrefixes" in data:
        import aws_sdk_direct_connect.types.route_filter_prefix_list

        out["route_filter_prefixes"] = (
            aws_sdk_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["routeFilterPrefixes"]
            )
        )
    if "bgpPeers" in data:
        import aws_sdk_direct_connect.types.bgp_peer_list

        out["bgp_peers"] = (
            aws_sdk_direct_connect.types.bgp_peer_list.deserialize_aws_json_1_1(
                data["bgpPeers"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    if "awsDeviceV2" in data:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if "awsLogicalDeviceId" in data:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if "tags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "siteLinkEnabled" in data:
        out["site_link_enabled"] = data["siteLinkEnabled"]
    return out
