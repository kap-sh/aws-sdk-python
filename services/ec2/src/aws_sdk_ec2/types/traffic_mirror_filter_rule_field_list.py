"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterRuleFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_field

TrafficMirrorFilterRuleFieldList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_filter_rule_field.TrafficMirrorFilterRuleField"
]
