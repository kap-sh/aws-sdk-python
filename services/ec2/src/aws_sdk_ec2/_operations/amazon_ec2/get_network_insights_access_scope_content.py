"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkInsightsAccessScopeContent``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_network_insights_access_scope_content_request
    import aws_sdk_ec2.types.get_network_insights_access_scope_content_result


def get_network_insights_access_scope_content(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_network_insights_access_scope_content_request.GetNetworkInsightsAccessScopeContentRequest,
) -> tuple[
    aws_sdk_ec2.types.get_network_insights_access_scope_content_result.GetNetworkInsightsAccessScopeContentResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_network_insights_access_scope_content(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_network_insights_access_scope_content_request.GetNetworkInsightsAccessScopeContentRequest,
) -> tuple[
    aws_sdk_ec2.types.get_network_insights_access_scope_content_result.GetNetworkInsightsAccessScopeContentResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
