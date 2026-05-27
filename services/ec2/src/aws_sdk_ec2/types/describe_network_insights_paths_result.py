"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsPathsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_path_list
    import aws_sdk_ec2.types.string


class DescribeNetworkInsightsPathsResult(TypedDict):
    network_insights_paths: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_list.NetworkInsightsPathList"
    ]
    """<p>Information about the paths.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
