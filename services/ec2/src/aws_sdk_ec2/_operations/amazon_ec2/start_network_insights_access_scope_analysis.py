"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAccessScopeAnalysis``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.start_network_insights_access_scope_analysis_request
    import aws_sdk_ec2.types.start_network_insights_access_scope_analysis_result


def start_network_insights_access_scope_analysis(
    options: OperationOptions,
    input: aws_sdk_ec2.types.start_network_insights_access_scope_analysis_request.StartNetworkInsightsAccessScopeAnalysisRequest,
) -> tuple[
    aws_sdk_ec2.types.start_network_insights_access_scope_analysis_result.StartNetworkInsightsAccessScopeAnalysisResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_start_network_insights_access_scope_analysis(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.start_network_insights_access_scope_analysis_request.StartNetworkInsightsAccessScopeAnalysisRequest,
) -> tuple[
    aws_sdk_ec2.types.start_network_insights_access_scope_analysis_result.StartNetworkInsightsAccessScopeAnalysisResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
