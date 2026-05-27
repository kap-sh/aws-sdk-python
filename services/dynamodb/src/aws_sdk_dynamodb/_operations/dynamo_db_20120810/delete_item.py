"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteItem``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.delete_item_input
    import aws_sdk_dynamodb.types.delete_item_output


def delete_item(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.delete_item_input.DeleteItemInput,
) -> tuple[aws_sdk_dynamodb.types.delete_item_output.DeleteItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_item(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.delete_item_input.DeleteItemInput,
) -> tuple[aws_sdk_dynamodb.types.delete_item_output.DeleteItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
