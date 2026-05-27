"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeEndpoints``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_endpoints_request
    import aws_sdk_dynamodb.types.describe_endpoints_response


def describe_endpoints(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_endpoints_request.DescribeEndpointsRequest,
) -> tuple[
    aws_sdk_dynamodb.types.describe_endpoints_response.DescribeEndpointsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_endpoints(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_endpoints_request.DescribeEndpointsRequest,
) -> tuple[
    aws_sdk_dynamodb.types.describe_endpoints_response.DescribeEndpointsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
