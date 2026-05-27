"""Generated from Smithy shape ``com.amazonaws.dynamodb#PutItem``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.put_item_input
    import aws_sdk_dynamodb.types.put_item_output


def put_item(
    options: OperationOptions, input: aws_sdk_dynamodb.types.put_item_input.PutItemInput
) -> tuple[aws_sdk_dynamodb.types.put_item_output.PutItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_item(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.put_item_input.PutItemInput,
) -> tuple[aws_sdk_dynamodb.types.put_item_output.PutItemOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
