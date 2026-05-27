"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateExpressGatewayService``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_express_gateway_service_request
    import aws_sdk_ecs.types.update_express_gateway_service_response


def update_express_gateway_service(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_express_gateway_service(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest,
) -> tuple[
    aws_sdk_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
