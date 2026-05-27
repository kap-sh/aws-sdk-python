"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkInsightsAccessScopeAnalysisFindings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_request
    import aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_result


def get_network_insights_access_scope_analysis_findings(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_request.GetNetworkInsightsAccessScopeAnalysisFindingsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_result.GetNetworkInsightsAccessScopeAnalysisFindingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_network_insights_access_scope_analysis_findings(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_request.GetNetworkInsightsAccessScopeAnalysisFindingsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_result.GetNetworkInsightsAccessScopeAnalysisFindingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
