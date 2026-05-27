"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorTargetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_target_set


class DescribeTrafficMirrorTargetsResult(TypedDict):
    traffic_mirror_targets: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_target_set.TrafficMirrorTargetSet"
    ]
    """<p>Information about one or more Traffic Mirror targets.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""
