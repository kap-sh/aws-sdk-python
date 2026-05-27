"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceDeployments``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_service_deployments_request
    import aws_sdk_ecs.types.describe_service_deployments_response


def describe_service_deployments(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_service_deployments(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
