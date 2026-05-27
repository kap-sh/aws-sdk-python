"""Generated from Smithy shape ``com.amazonaws.ecs#DiscoverPollEndpoint``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.discover_poll_endpoint_request
    import aws_sdk_ecs.types.discover_poll_endpoint_response


def discover_poll_endpoint(
    options: OperationOptions,
    input: aws_sdk_ecs.types.discover_poll_endpoint_request.DiscoverPollEndpointRequest,
) -> tuple[
    aws_sdk_ecs.types.discover_poll_endpoint_response.DiscoverPollEndpointResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_discover_poll_endpoint(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.discover_poll_endpoint_request.DiscoverPollEndpointRequest,
) -> tuple[
    aws_sdk_ecs.types.discover_poll_endpoint_response.DiscoverPollEndpointResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
