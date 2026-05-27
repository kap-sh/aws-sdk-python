"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetItem``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.get_item_input
    import aws_sdk_dynamodb.types.get_item_output


def get_item(
    options: OperationOptions, input: aws_sdk_dynamodb.types.get_item_input.GetItemInput
) -> tuple[aws_sdk_dynamodb.types.get_item_output.GetItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_item(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.get_item_input.GetItemInput,
) -> tuple[aws_sdk_dynamodb.types.get_item_output.GetItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
