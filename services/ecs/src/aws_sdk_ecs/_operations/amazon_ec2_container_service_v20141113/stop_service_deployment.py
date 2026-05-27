"""Generated from Smithy shape ``com.amazonaws.ecs#StopServiceDeployment``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.stop_service_deployment_request
    import aws_sdk_ecs.types.stop_service_deployment_response


def stop_service_deployment(
    options: OperationOptions,
    input: aws_sdk_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest,
) -> tuple[
    aws_sdk_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_stop_service_deployment(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest,
) -> tuple[
    aws_sdk_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
