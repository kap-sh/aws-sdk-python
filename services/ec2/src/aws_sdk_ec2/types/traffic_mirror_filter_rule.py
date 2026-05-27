"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.traffic_direction
    import aws_sdk_ec2.types.traffic_mirror_port_range
    import aws_sdk_ec2.types.traffic_mirror_rule_action


class TrafficMirrorFilterRule(TypedDict):
    traffic_mirror_filter_rule_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror rule.</p>"""
    traffic_mirror_filter_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter that the rule is associated with.</p>"""
    traffic_direction: NotRequired[
        "aws_sdk_ec2.types.traffic_direction.TrafficDirection"
    ]
    """<p>The traffic direction assigned to the Traffic Mirror rule.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number of the Traffic Mirror rule.</p>"""
    rule_action: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_rule_action.TrafficMirrorRuleAction"
    ]
    """<p>The action assigned to the Traffic Mirror rule.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The protocol assigned to the Traffic Mirror rule.</p>"""
    destination_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range.TrafficMirrorPortRange"
    ]
    """<p>The destination port range assigned to the Traffic Mirror rule.</p>"""
    source_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range.TrafficMirrorPortRange"
    ]
    """<p>The source port range assigned to the Traffic Mirror rule.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block assigned to the Traffic Mirror rule.</p>"""
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block assigned to the Traffic Mirror rule.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror rule.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Tags on Traffic Mirroring filter rules.</p>"""
