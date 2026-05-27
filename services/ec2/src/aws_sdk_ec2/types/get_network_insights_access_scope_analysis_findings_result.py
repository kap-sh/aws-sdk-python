"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkInsightsAccessScopeAnalysisFindingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_analysis_finding_list
    import aws_sdk_ec2.types.analysis_status
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id
    import aws_sdk_ec2.types.string


class GetNetworkInsightsAccessScopeAnalysisFindingsResult(TypedDict):
    network_insights_access_scope_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    analysis_status: NotRequired["aws_sdk_ec2.types.analysis_status.AnalysisStatus"]
    """<p>The status of Network Access Scope Analysis.</p>"""
    analysis_findings: NotRequired[
        "aws_sdk_ec2.types.access_scope_analysis_finding_list.AccessScopeAnalysisFindingList"
    ]
    """<p>The findings associated with Network Access Scope Analysis.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
