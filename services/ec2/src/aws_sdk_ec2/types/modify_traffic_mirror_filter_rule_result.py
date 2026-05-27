"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterRuleResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter_rule


class ModifyTrafficMirrorFilterRuleResult(TypedDict):
    traffic_mirror_filter_rule: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule.TrafficMirrorFilterRule"
    ]
    """<note> <p>Tags are not returned for ModifyTrafficMirrorFilterRule.</p> </note> <p>A Traffic Mirror rule.</p>"""
