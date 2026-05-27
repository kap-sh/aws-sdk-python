"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeCapacityProviders``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_capacity_providers_request
    import aws_sdk_ecs.types.describe_capacity_providers_response


def describe_capacity_providers(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_capacity_providers(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
