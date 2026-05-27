"""Generated from Smithy shape ``com.amazonaws.dynamodb#TagResource``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.tag_resource_input


def tag_resource(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.tag_resource_input.TagResourceInput,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_tag_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.tag_resource_input.TagResourceInput,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
