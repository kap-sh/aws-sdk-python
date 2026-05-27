"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorFiltersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_filter_set


class DescribeTrafficMirrorFiltersResult(TypedDict):
    traffic_mirror_filters: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_set.TrafficMirrorFilterSet"
    ]
    """<p>Information about one or more Traffic Mirror filters.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""
