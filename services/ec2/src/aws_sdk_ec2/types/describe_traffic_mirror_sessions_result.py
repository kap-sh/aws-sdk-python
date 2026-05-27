"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorSessionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_session_set


class DescribeTrafficMirrorSessionsResult(TypedDict):
    traffic_mirror_sessions: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session_set.TrafficMirrorSessionSet"
    ]
    """<p>Describes one or more Traffic Mirror sessions. By default, all Traffic Mirror sessions are described. Alternatively, you can filter the results.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""
