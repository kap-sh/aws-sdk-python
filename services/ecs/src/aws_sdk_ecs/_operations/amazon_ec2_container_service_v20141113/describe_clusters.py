"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeClusters``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_clusters_request
    import aws_sdk_ecs.types.describe_clusters_response


def describe_clusters(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_clusters_request.DescribeClustersRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_clusters_response.DescribeClustersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_clusters(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_clusters_request.DescribeClustersRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_clusters_response.DescribeClustersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
