"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchWriteItem``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.batch_write_item_input
    import aws_sdk_dynamodb.types.batch_write_item_output


def batch_write_item(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.batch_write_item_input.BatchWriteItemInput,
) -> tuple[
    aws_sdk_dynamodb.types.batch_write_item_output.BatchWriteItemOutput, zapros.Response
]:
    raise NotImplementedError("operationContextParams JMESPath not yet supported")


async def async_batch_write_item(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.batch_write_item_input.BatchWriteItemInput,
) -> tuple[
    aws_sdk_dynamodb.types.batch_write_item_output.BatchWriteItemOutput, zapros.Response
]:
    raise NotImplementedError("operationContextParams JMESPath not yet supported")
