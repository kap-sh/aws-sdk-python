"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_direction
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver
    import aws_sdk_ec2.types.traffic_mirror_port_range_request
    import aws_sdk_ec2.types.traffic_mirror_rule_action


class ModifyTrafficMirrorFilterRuleRequest(TypedDict):
    traffic_mirror_filter_rule_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver.TrafficMirrorFilterRuleIdWithResolver"
    ]
    """<p>The ID of the Traffic Mirror rule.</p>"""
    traffic_direction: NotRequired[
        "aws_sdk_ec2.types.traffic_direction.TrafficDirection"
    ]
    """<p>The type of traffic to assign to the rule.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.</p>"""
    rule_action: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_rule_action.TrafficMirrorRuleAction"
    ]
    """<p>The action to assign to the rule.</p>"""
    destination_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The destination ports that are associated with the Traffic Mirror rule.</p>"""
    source_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The port range to assign to the Traffic Mirror rule.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The protocol, for example TCP, to assign to the Traffic Mirror rule.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block to assign to the Traffic Mirror rule.</p>"""
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block to assign to the Traffic Mirror rule.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description to assign to the Traffic Mirror rule.</p>"""
    remove_fields: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list.TrafficMirrorFilterRuleFieldList"
    ]
    """<p>The properties that you want to remove from the Traffic Mirror filter rule.</p> <p>When you remove a property from a Traffic Mirror filter rule, the property is set to the default.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
