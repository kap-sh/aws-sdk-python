"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateService``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_service_request
    import aws_sdk_ecs.types.update_service_response


def update_service(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_service_request.UpdateServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.update_service_response.UpdateServiceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_service(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_service_request.UpdateServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.update_service_response.UpdateServiceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
