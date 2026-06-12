"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteBGPPeerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.asn
    import aws_sdk_direct_connect.types.bgp_peer_id
    import aws_sdk_direct_connect.types.customer_address
    import aws_sdk_direct_connect.types.long_asn
    import aws_sdk_direct_connect.types.virtual_interface_id


class DeleteBGPPeerRequest(TypedDict):
    virtual_interface_id: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    asn: "aws_sdk_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    asn_long: NotRequired["aws_sdk_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for the BGP peer to be deleted from a Direct Connect virtual interface. The valid range is from 1 to 4294967294 for BGP configuration. </p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>"""
    customer_address: NotRequired[
        "aws_sdk_direct_connect.types.customer_address.CustomerAddress"
    ]
    """<p>The IP address assigned to the customer interface.</p>"""
    bgp_peer_id: NotRequired["aws_sdk_direct_connect.types.bgp_peer_id.BGPPeerId"]
    """<p>The ID of the BGP peer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBGPPeerRequest) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "bgp_peer_id" in value:
        out["bgpPeerId"] = value["bgp_peer_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBGPPeerRequest:
    out: DeleteBGPPeerRequest = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if "asn" in data:
        out["asn"] = data["asn"]
    else:
        out["asn"] = 0
    if "asnLong" in data:
        out["asn_long"] = data["asnLong"]
    if "customerAddress" in data:
        out["customer_address"] = data["customerAddress"]
    if "bgpPeerId" in data:
        out["bgp_peer_id"] = data["bgpPeerId"]
    return out
