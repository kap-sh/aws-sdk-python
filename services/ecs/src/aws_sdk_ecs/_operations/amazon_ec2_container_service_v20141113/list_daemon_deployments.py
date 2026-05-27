"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonDeployments``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_daemon_deployments_request
    import aws_sdk_ecs.types.list_daemon_deployments_response


def list_daemon_deployments(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest,
) -> tuple[
    aws_sdk_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_daemon_deployments(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest,
) -> tuple[
    aws_sdk_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
