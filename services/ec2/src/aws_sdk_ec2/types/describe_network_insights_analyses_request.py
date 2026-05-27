"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAnalysesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_analysis_id_list
    import aws_sdk_ec2.types.network_insights_max_results
    import aws_sdk_ec2.types.network_insights_path_id
    import aws_sdk_ec2.types.next_token


class DescribeNetworkInsightsAnalysesRequest(TypedDict):
    network_insights_analysis_ids: NotRequired[
        "aws_sdk_ec2.types.network_insights_analysis_id_list.NetworkInsightsAnalysisIdList"
    ]
    """<p>The ID of the network insights analyses. You must specify either analysis IDs or a path ID.</p>"""
    network_insights_path_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path. You must specify either a path ID or analysis IDs.</p>"""
    analysis_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time when the network insights analyses started.</p>"""
    analysis_end_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time when the network insights analyses ended.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters. The following are the possible values:</p> <ul> <li> <p>path-found - A Boolean value that indicates whether a feasible path is found.</p> </li> <li> <p>status - The status of the analysis (running | succeeded | failed).</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.network_insights_max_results.NetworkInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
