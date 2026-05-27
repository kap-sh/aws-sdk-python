"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServices``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_services_request
    import aws_sdk_ecs.types.describe_services_response


def describe_services(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_services_request.DescribeServicesRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_services_response.DescribeServicesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_services(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_services_request.DescribeServicesRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_services_response.DescribeServicesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
