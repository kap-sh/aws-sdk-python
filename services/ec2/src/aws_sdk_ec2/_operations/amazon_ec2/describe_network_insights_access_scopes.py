"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAccessScopes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_network_insights_access_scopes_request
    import aws_sdk_ec2.types.describe_network_insights_access_scopes_result


def describe_network_insights_access_scopes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_network_insights_access_scopes_request.DescribeNetworkInsightsAccessScopesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_network_insights_access_scopes_result.DescribeNetworkInsightsAccessScopesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_network_insights_access_scopes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_network_insights_access_scopes_request.DescribeNetworkInsightsAccessScopesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_network_insights_access_scopes_result.DescribeNetworkInsightsAccessScopesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
