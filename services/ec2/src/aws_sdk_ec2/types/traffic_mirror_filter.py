"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_list
    import aws_sdk_ec2.types.traffic_mirror_network_service_list


class TrafficMirrorFilter(TypedDict):
    traffic_mirror_filter_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    ingress_filter_rules: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_list.TrafficMirrorFilterRuleList"
    ]
    """<p>Information about the ingress rules that are associated with the Traffic Mirror filter.</p>"""
    egress_filter_rules: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_list.TrafficMirrorFilterRuleList"
    ]
    """<p>Information about the egress rules that are associated with the Traffic Mirror filter.</p>"""
    network_services: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_network_service_list.TrafficMirrorNetworkServiceList"
    ]
    """<p>The network service traffic that is associated with the Traffic Mirror filter.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror filter.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Traffic Mirror filter.</p>"""
