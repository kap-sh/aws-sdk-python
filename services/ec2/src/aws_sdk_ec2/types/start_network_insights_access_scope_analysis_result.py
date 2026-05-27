"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAccessScopeAnalysisResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_analysis


class StartNetworkInsightsAccessScopeAnalysisResult(TypedDict):
    network_insights_access_scope_analysis: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis.NetworkInsightsAccessScopeAnalysis"
    ]
    """<p>The Network Access Scope analysis.</p>"""
