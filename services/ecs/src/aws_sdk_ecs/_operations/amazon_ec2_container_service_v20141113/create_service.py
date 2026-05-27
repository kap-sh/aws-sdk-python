"""Generated from Smithy shape ``com.amazonaws.ecs#CreateService``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.create_service_request
    import aws_sdk_ecs.types.create_service_response


def create_service(
    options: OperationOptions,
    input: aws_sdk_ecs.types.create_service_request.CreateServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.create_service_response.CreateServiceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_service(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.create_service_request.CreateServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.create_service_response.CreateServiceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
