"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkInsightsAccessScopeAnalysisFindingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_max_results
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id
    import aws_sdk_ec2.types.next_token


class GetNetworkInsightsAccessScopeAnalysisFindingsRequest(TypedDict):
    network_insights_access_scope_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_max_results.GetNetworkInsightsAccessScopeAnalysisFindingsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
