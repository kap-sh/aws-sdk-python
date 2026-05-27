"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.traffic_mirror_filter_id
    import aws_sdk_ec2.types.traffic_mirror_target_id


class CreateTrafficMirrorSessionRequest(TypedDict):
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the source network interface.</p>"""
    traffic_mirror_target_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_target_id.TrafficMirrorTargetId"
    ]
    """<p>The ID of the Traffic Mirror target.</p>"""
    traffic_mirror_filter_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    packet_length: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of bytes in each packet to mirror. These are bytes after the VXLAN header. Do not specify this parameter when you want to mirror the entire packet. To mirror a subset of the packet, set this to the length (in bytes) that you want to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target.</p> <p>If you do not want to mirror the entire packet, use the <code>PacketLength</code> parameter to specify the number of bytes in each packet to mirror.</p> <p>For sessions with Network Load Balancer (NLB) Traffic Mirror targets the default <code>PacketLength</code> will be set to 8500. Valid values are 1-8500. Setting a <code>PacketLength</code> greater than 8500 will result in an error response.</p>"""
    session_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.</p> <p>Valid values are 1-32766.</p>"""
    virtual_network_id: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The VXLAN ID for the Traffic Mirror session. For more information about the VXLAN protocol, see <a href=\"https://datatracker.ietf.org/doc/html/rfc7348\">RFC 7348</a>. If you do not specify a <code>VirtualNetworkId</code>, an account-wide unique ID is chosen at random.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror session.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to a Traffic Mirror session.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
