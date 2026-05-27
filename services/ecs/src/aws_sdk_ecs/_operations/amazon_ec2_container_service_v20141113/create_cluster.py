"""Generated from Smithy shape ``com.amazonaws.ecs#CreateCluster``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.create_cluster_request
    import aws_sdk_ecs.types.create_cluster_response


def create_cluster(
    options: OperationOptions,
    input: aws_sdk_ecs.types.create_cluster_request.CreateClusterRequest,
) -> tuple[
    aws_sdk_ecs.types.create_cluster_response.CreateClusterResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_cluster(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.create_cluster_request.CreateClusterRequest,
) -> tuple[
    aws_sdk_ecs.types.create_cluster_response.CreateClusterResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
