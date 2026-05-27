"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteCluster``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_cluster_request
    import aws_sdk_ecs.types.delete_cluster_response


def delete_cluster(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_cluster_request.DeleteClusterRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_cluster_response.DeleteClusterResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_cluster(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_cluster_request.DeleteClusterRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_cluster_response.DeleteClusterResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
