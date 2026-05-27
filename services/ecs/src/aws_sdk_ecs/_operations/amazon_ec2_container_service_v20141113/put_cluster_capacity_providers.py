"""Generated from Smithy shape ``com.amazonaws.ecs#PutClusterCapacityProviders``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.put_cluster_capacity_providers_request
    import aws_sdk_ecs.types.put_cluster_capacity_providers_response


def put_cluster_capacity_providers(
    options: OperationOptions,
    input: aws_sdk_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest,
) -> tuple[
    aws_sdk_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_cluster_capacity_providers(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest,
) -> tuple[
    aws_sdk_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
