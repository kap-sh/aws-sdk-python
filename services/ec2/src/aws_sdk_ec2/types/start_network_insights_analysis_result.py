"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAnalysisResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_analysis


class StartNetworkInsightsAnalysisResult(TypedDict):
    network_insights_analysis: NotRequired[
        "aws_sdk_ec2.types.network_insights_analysis.NetworkInsightsAnalysis"
    ]
    """<p>Information about the network insights analysis.</p>"""
