"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateCluster``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_cluster_request
    import aws_sdk_ecs.types.update_cluster_response


def update_cluster(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_cluster_request.UpdateClusterRequest,
) -> tuple[
    aws_sdk_ecs.types.update_cluster_response.UpdateClusterResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_cluster(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_cluster_request.UpdateClusterRequest,
) -> tuple[
    aws_sdk_ecs.types.update_cluster_response.UpdateClusterResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
