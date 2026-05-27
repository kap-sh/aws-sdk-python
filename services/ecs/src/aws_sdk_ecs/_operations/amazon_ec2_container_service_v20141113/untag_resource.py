"""Generated from Smithy shape ``com.amazonaws.ecs#UntagResource``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.untag_resource_request
    import aws_sdk_ecs.types.untag_resource_response


def untag_resource(
    options: OperationOptions,
    input: aws_sdk_ecs.types.untag_resource_request.UntagResourceRequest,
) -> tuple[
    aws_sdk_ecs.types.untag_resource_response.UntagResourceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_untag_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.untag_resource_request.UntagResourceRequest,
) -> tuple[
    aws_sdk_ecs.types.untag_resource_response.UntagResourceResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
