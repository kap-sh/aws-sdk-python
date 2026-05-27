"""Generated from Smithy shape ``com.amazonaws.ecs#ListAttributes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_attributes_request
    import aws_sdk_ecs.types.list_attributes_response


def list_attributes(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_attributes_request.ListAttributesRequest,
) -> tuple[
    aws_sdk_ecs.types.list_attributes_response.ListAttributesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_attributes(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_attributes_request.ListAttributesRequest,
) -> tuple[
    aws_sdk_ecs.types.list_attributes_response.ListAttributesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
