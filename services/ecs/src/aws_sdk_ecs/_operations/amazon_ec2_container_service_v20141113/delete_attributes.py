"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAttributes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_attributes_request
    import aws_sdk_ecs.types.delete_attributes_response


def delete_attributes(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_attributes_request.DeleteAttributesRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_attributes_response.DeleteAttributesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_attributes(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_attributes_request.DeleteAttributesRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_attributes_response.DeleteAttributesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
