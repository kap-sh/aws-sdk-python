"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.amazon_address
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.aws_device_v2
    import capo_direct_connect.types.aws_logical_device_id
    import capo_direct_connect.types.bgp_auth_key
    import capo_direct_connect.types.bgp_peer_id
    import capo_direct_connect.types.bgp_peer_state
    import capo_direct_connect.types.bgp_status
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.long_asn


class BGPPeer(TypedDict, closed=True):
    bgp_peer_id: NotRequired["capo_direct_connect.types.bgp_peer_id.BGPPeerId"]
    """<p>The ID of the BGP peer.</p>"""
    asn: "capo_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    asn_long: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for the BGP peer. The valid range is from 1 to 4294967294 for BGP configuration. </p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    auth_key: NotRequired["capo_direct_connect.types.bgp_auth_key.BGPAuthKey"]
    """<p>The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.</p>"""
    address_family: NotRequired[
        "capo_direct_connect.types.address_family.AddressFamily"
    ]
    """<p>The address family for the BGP peer.</p>"""
    amazon_address: NotRequired[
        "capo_direct_connect.types.amazon_address.AmazonAddress"
    ]
    """<p>The IP address assigned to the Amazon interface.</p>"""
    customer_address: NotRequired[
        "capo_direct_connect.types.customer_address.CustomerAddress"
    ]
    """<p>The IP address assigned to the customer interface.</p>"""
    bgp_peer_state: NotRequired["capo_direct_connect.types.bgp_peer_state.BGPPeerState"]
    """<p>The state of the BGP peer. The following are the possible values:</p> <ul> <li> <p> <code>verifying</code>: The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.</p> </li> <li> <p> <code>pending</code>: The BGP peer is created, and remains in this state until it is ready to be established.</p> </li> <li> <p> <code>available</code>: The BGP peer is ready to be established.</p> </li> <li> <p> <code>deleting</code>: The BGP peer is being deleted.</p> </li> <li> <p> <code>deleted</code>: The BGP peer is deleted and cannot be established.</p> </li> </ul>"""
    bgp_status: NotRequired["capo_direct_connect.types.bgp_status.BGPStatus"]
    """<p>The status of the BGP peer. The following are the possible values:</p> <ul> <li> <p> <code>up</code>: The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.</p> </li> <li> <p> <code>down</code>: The BGP peer is down.</p> </li> <li> <p> <code>unknown</code>: The BGP peer status is not available.</p> </li> </ul>"""
    aws_device_v2: NotRequired["capo_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that terminates the BGP peer.</p>"""
    aws_logical_device_id: NotRequired[
        "capo_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPPeer) -> dict:
    out: dict = {}
    if "bgp_peer_id" in value:
        out["bgpPeerId"] = value["bgp_peer_id"]
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "auth_key" in value:
        out["authKey"] = value["auth_key"]
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = (
            capo_direct_connect.types.address_family.serialize_aws_json_1_1(
                value["address_family"]
            )
        )
    if "amazon_address" in value:
        out["amazonAddress"] = value["amazon_address"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "bgp_peer_state" in value:
        import capo_direct_connect.types.bgp_peer_state

        out["bgpPeerState"] = (
            capo_direct_connect.types.bgp_peer_state.serialize_aws_json_1_1(
                value["bgp_peer_state"]
            )
        )
    if "bgp_status" in value:
        import capo_direct_connect.types.bgp_status

        out["bgpStatus"] = capo_direct_connect.types.bgp_status.serialize_aws_json_1_1(
            value["bgp_status"]
        )
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BGPPeer:
    out: BGPPeer = {}  # type: ignore[typeddict-item]
    if "bgpPeerId" in data:
        out["bgp_peer_id"] = data["bgpPeerId"]
    if "asn" in data:
        out["asn"] = data["asn"]
    else:
        out["asn"] = 0
    if "asnLong" in data:
        out["asn_long"] = data["asnLong"]
    if "authKey" in data:
        out["auth_key"] = data["authKey"]
    if "addressFamily" in data:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_aws_json_1_1(
                data["addressFamily"]
            )
        )
    if "amazonAddress" in data:
        out["amazon_address"] = data["amazonAddress"]
    if "customerAddress" in data:
        out["customer_address"] = data["customerAddress"]
    if "bgpPeerState" in data:
        import capo_direct_connect.types.bgp_peer_state

        out["bgp_peer_state"] = (
            capo_direct_connect.types.bgp_peer_state.deserialize_aws_json_1_1(
                data["bgpPeerState"]
            )
        )
    if "bgpStatus" in data:
        import capo_direct_connect.types.bgp_status

        out["bgp_status"] = (
            capo_direct_connect.types.bgp_status.deserialize_aws_json_1_1(
                data["bgpStatus"]
            )
        )
    if "awsDeviceV2" in data:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if "awsLogicalDeviceId" in data:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    return out
