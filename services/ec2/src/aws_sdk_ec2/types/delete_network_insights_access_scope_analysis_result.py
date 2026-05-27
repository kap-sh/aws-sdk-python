"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsAccessScopeAnalysisResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id


class DeleteNetworkInsightsAccessScopeAnalysisResult(TypedDict):
    network_insights_access_scope_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
