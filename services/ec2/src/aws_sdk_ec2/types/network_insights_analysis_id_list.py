"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAnalysisIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_analysis_id

NetworkInsightsAnalysisIdList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_analysis_id.NetworkInsightsAnalysisId"
]
