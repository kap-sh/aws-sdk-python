"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonDeployments``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_daemon_deployments_request
    import aws_sdk_ecs.types.describe_daemon_deployments_response


def describe_daemon_deployments(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_daemon_deployments(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
