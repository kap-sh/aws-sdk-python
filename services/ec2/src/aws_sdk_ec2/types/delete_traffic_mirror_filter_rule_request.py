"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver


class DeleteTrafficMirrorFilterRuleRequest(TypedDict):
    traffic_mirror_filter_rule_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver.TrafficMirrorFilterRuleIdWithResolver"
    ]
    """<p>The ID of the Traffic Mirror rule.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
