"""Generated from Smithy shape ``com.amazonaws.ecs#ListClusters``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_clusters_request
    import aws_sdk_ecs.types.list_clusters_response


def list_clusters(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_clusters_request.ListClustersRequest,
) -> tuple[
    aws_sdk_ecs.types.list_clusters_response.ListClustersResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_clusters(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_clusters_request.ListClustersRequest,
) -> tuple[
    aws_sdk_ecs.types.list_clusters_response.ListClustersResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
