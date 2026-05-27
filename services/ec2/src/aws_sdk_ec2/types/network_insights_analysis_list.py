"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAnalysisList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_analysis

NetworkInsightsAnalysisList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_analysis.NetworkInsightsAnalysis"
]
