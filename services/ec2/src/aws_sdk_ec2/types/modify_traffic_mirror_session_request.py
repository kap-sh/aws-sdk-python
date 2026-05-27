"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_filter_id
    import aws_sdk_ec2.types.traffic_mirror_session_field_list
    import aws_sdk_ec2.types.traffic_mirror_session_id
    import aws_sdk_ec2.types.traffic_mirror_target_id


class ModifyTrafficMirrorSessionRequest(TypedDict):
    traffic_mirror_session_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session_id.TrafficMirrorSessionId"
    ]
    """<p>The ID of the Traffic Mirror session.</p>"""
    traffic_mirror_target_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_target_id.TrafficMirrorTargetId"
    ]
    """<p>The Traffic Mirror target. The target must be in the same VPC as the source, or have a VPC peering connection with the source.</p>"""
    traffic_mirror_filter_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    packet_length: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of bytes in each packet to mirror. These are bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet.</p> <p>For sessions with Network Load Balancer (NLB) traffic mirror targets, the default <code>PacketLength</code> will be set to 8500. Valid values are 1-8500. Setting a <code>PacketLength</code> greater than 8500 will result in an error response.</p>"""
    session_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.</p> <p>Valid values are 1-32766.</p>"""
    virtual_network_id: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The virtual network ID of the Traffic Mirror session.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description to assign to the Traffic Mirror session.</p>"""
    remove_fields: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session_field_list.TrafficMirrorSessionFieldList"
    ]
    """<p>The properties that you want to remove from the Traffic Mirror session.</p> <p>When you remove a property from a Traffic Mirror session, the property is set to the default.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
