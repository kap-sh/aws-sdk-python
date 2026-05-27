"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.traffic_mirror_target_type


class TrafficMirrorTarget(TypedDict):
    traffic_mirror_target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror target.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The network interface ID that is attached to the target.</p>"""
    network_load_balancer_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Network Load Balancer.</p>"""
    type: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_target_type.TrafficMirrorTargetType"
    ]
    """<p>The type of Traffic Mirror target.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Information about the Traffic Mirror target.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that owns the Traffic Mirror target.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Traffic Mirror target.</p>"""
    gateway_load_balancer_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Gateway Load Balancer endpoint.</p>"""
