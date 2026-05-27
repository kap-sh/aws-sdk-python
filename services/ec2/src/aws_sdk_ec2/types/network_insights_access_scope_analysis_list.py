"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeAnalysisList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_analysis

NetworkInsightsAccessScopeAnalysisList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_access_scope_analysis.NetworkInsightsAccessScopeAnalysis"
]
