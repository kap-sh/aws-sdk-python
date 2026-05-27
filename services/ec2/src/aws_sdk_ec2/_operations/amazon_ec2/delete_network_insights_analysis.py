"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsAnalysis``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_network_insights_analysis_request
    import aws_sdk_ec2.types.delete_network_insights_analysis_result


def delete_network_insights_analysis(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_network_insights_analysis_request.DeleteNetworkInsightsAnalysisRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_network_insights_analysis_result.DeleteNetworkInsightsAnalysisResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_network_insights_analysis(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_network_insights_analysis_request.DeleteNetworkInsightsAnalysisRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_network_insights_analysis_result.DeleteNetworkInsightsAnalysisResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
