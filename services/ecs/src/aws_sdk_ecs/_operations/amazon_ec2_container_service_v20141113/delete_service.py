"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteService``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_service_request
    import aws_sdk_ecs.types.delete_service_response


def delete_service(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_service_request.DeleteServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_service_response.DeleteServiceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_service(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_service_request.DeleteServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_service_response.DeleteServiceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
