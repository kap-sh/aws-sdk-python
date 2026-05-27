"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBgpOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.route_server_peer_liveness_mode


class RouteServerBgpOptionsRequest(TypedDict):
    peer_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.</p>"""
    peer_liveness_detection: NotRequired[
        "aws_sdk_ec2.types.route_server_peer_liveness_mode.RouteServerPeerLivenessMode"
    ]
    """<p>The requested liveness detection protocol for the BGP peer.</p> <ul> <li> <p> <code>bgp-keepalive</code>: The standard BGP keep alive mechanism (<a href=\"https://www.rfc-editor.org/rfc/rfc4271#page-21\">RFC4271</a>) that is stable but may take longer to fail-over in cases of network impact or router failure.</p> </li> <li> <p> <code>bfd</code>: An additional Bidirectional Forwarding Detection (BFD) protocol (<a href=\"https://www.rfc-editor.org/rfc/rfc5880\">RFC5880</a>) that enables fast failover by using more sensitive liveness detection.</p> </li> </ul> <p>Defaults to <code>bgp-keepalive</code>.</p>"""
