"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorSession``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class TrafficMirrorSession(TypedDict):
    traffic_mirror_session_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID for the Traffic Mirror session.</p>"""
    traffic_mirror_target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror target.</p>"""
    traffic_mirror_filter_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror session's network interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that owns the Traffic Mirror session.</p>"""
    packet_length: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of bytes in each packet to mirror. These are the bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet</p>"""
    session_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.</p> <p>Valid values are 1-32766.</p>"""
    virtual_network_id: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The virtual network ID associated with the Traffic Mirror session.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror session.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Traffic Mirror session.</p>"""
