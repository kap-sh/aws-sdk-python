"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsAnalysisResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_analysis_id


class DeleteNetworkInsightsAnalysisResult(TypedDict):
    network_insights_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_analysis_id.NetworkInsightsAnalysisId"
    ]
    """<p>The ID of the network insights analysis.</p>"""
