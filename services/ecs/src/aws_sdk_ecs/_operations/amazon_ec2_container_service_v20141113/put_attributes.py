"""Generated from Smithy shape ``com.amazonaws.ecs#PutAttributes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.put_attributes_request
    import aws_sdk_ecs.types.put_attributes_response


def put_attributes(
    options: OperationOptions,
    input: aws_sdk_ecs.types.put_attributes_request.PutAttributesRequest,
) -> tuple[
    aws_sdk_ecs.types.put_attributes_response.PutAttributesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_attributes(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.put_attributes_request.PutAttributesRequest,
) -> tuple[
    aws_sdk_ecs.types.put_attributes_response.PutAttributesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
