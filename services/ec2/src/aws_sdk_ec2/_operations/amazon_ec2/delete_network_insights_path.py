"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsPath``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_network_insights_path_request
    import aws_sdk_ec2.types.delete_network_insights_path_result


def delete_network_insights_path(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_network_insights_path_request.DeleteNetworkInsightsPathRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_network_insights_path_result.DeleteNetworkInsightsPathResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_network_insights_path(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_network_insights_path_request.DeleteNetworkInsightsPathRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_network_insights_path_result.DeleteNetworkInsightsPathResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
