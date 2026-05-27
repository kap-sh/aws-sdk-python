"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsPaths``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_network_insights_paths_request
    import aws_sdk_ec2.types.describe_network_insights_paths_result


def describe_network_insights_paths(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_network_insights_paths_request.DescribeNetworkInsightsPathsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_network_insights_paths_result.DescribeNetworkInsightsPathsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_network_insights_paths(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_network_insights_paths_request.DescribeNetworkInsightsPathsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_network_insights_paths_result.DescribeNetworkInsightsPathsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
