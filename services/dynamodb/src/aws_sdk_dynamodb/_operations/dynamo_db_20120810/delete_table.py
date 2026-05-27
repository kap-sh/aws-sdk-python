"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteTable``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.delete_table_input
    import aws_sdk_dynamodb.types.delete_table_output


def delete_table(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.delete_table_input.DeleteTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.delete_table_output.DeleteTableOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_table(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.delete_table_input.DeleteTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.delete_table_output.DeleteTableOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
