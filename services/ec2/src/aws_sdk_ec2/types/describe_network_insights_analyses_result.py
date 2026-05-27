"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAnalysesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_analysis_list
    import aws_sdk_ec2.types.string


class DescribeNetworkInsightsAnalysesResult(TypedDict):
    network_insights_analyses: NotRequired[
        "aws_sdk_ec2.types.network_insights_analysis_list.NetworkInsightsAnalysisList"
    ]
    """<p>Information about the network insights analyses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
