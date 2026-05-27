"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsAccessScope``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_network_insights_access_scope_request
    import aws_sdk_ec2.types.create_network_insights_access_scope_result


def create_network_insights_access_scope(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_network_insights_access_scope_request.CreateNetworkInsightsAccessScopeRequest,
) -> tuple[
    aws_sdk_ec2.types.create_network_insights_access_scope_result.CreateNetworkInsightsAccessScopeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_network_insights_access_scope(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_network_insights_access_scope_request.CreateNetworkInsightsAccessScopeRequest,
) -> tuple[
    aws_sdk_ec2.types.create_network_insights_access_scope_result.CreateNetworkInsightsAccessScopeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
