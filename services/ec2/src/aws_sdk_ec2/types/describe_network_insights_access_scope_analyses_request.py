"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAccessScopeAnalysesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.network_insights_max_results
    import aws_sdk_ec2.types.next_token


class DescribeNetworkInsightsAccessScopeAnalysesRequest(TypedDict):
    network_insights_access_scope_analysis_ids: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list.NetworkInsightsAccessScopeAnalysisIdList"
    ]
    """<p>The IDs of the Network Access Scope analyses.</p>"""
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    analysis_start_time_begin: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Filters the results based on the start time. The analysis must have started on or after this time.</p>"""
    analysis_start_time_end: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Filters the results based on the start time. The analysis must have started on or before this time.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>There are no supported filters.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.network_insights_max_results.NetworkInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
