"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteExpressGatewayService``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_express_gateway_service_request
    import aws_sdk_ecs.types.delete_express_gateway_service_response


def delete_express_gateway_service(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_express_gateway_service(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
