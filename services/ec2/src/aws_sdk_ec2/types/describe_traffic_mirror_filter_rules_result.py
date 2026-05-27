"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorFilterRulesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_set


class DescribeTrafficMirrorFilterRulesResult(TypedDict):
    traffic_mirror_filter_rules: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_set.TrafficMirrorFilterRuleSet"
    ]
    """<p>Traffic mirror rules.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""
