"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateItem``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.update_item_input
    import aws_sdk_dynamodb.types.update_item_output


def update_item(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.update_item_input.UpdateItemInput,
) -> tuple[aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_item(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.update_item_input.UpdateItemInput,
) -> tuple[aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
