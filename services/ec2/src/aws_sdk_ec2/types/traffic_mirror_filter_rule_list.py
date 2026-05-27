"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter_rule

TrafficMirrorFilterRuleList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_filter_rule.TrafficMirrorFilterRule"
]
