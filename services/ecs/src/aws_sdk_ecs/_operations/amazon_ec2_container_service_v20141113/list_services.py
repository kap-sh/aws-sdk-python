"""Generated from Smithy shape ``com.amazonaws.ecs#ListServices``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_services_request
    import aws_sdk_ecs.types.list_services_response


def list_services(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_services_request.ListServicesRequest,
) -> tuple[
    aws_sdk_ecs.types.list_services_response.ListServicesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_services(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_services_request.ListServicesRequest,
) -> tuple[
    aws_sdk_ecs.types.list_services_response.ListServicesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
