"""Generated from Smithy shape ``com.amazonaws.ecs#ListTagsForResource``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_tags_for_resource_request
    import aws_sdk_ecs.types.list_tags_for_resource_response


def list_tags_for_resource(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    aws_sdk_ecs.types.list_tags_for_resource_response.ListTagsForResourceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_tags_for_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    aws_sdk_ecs.types.list_tags_for_resource_response.ListTagsForResourceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
