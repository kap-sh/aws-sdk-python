"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItems``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.transact_write_items_input
    import aws_sdk_dynamodb.types.transact_write_items_output


def transact_write_items(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.transact_write_items_input.TransactWriteItemsInput,
) -> tuple[
    aws_sdk_dynamodb.types.transact_write_items_output.TransactWriteItemsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operationContextParams JMESPath not yet supported")


async def async_transact_write_items(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.transact_write_items_input.TransactWriteItemsInput,
) -> tuple[
    aws_sdk_dynamodb.types.transact_write_items_output.TransactWriteItemsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operationContextParams JMESPath not yet supported")
