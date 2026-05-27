"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportTable``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_table_input
    import aws_sdk_dynamodb.types.import_table_output


def import_table(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.import_table_input.ImportTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.import_table_output.ImportTableOutput, zapros.Response
]:
    raise NotImplementedError("operationContextParams JMESPath not yet supported")


async def async_import_table(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.import_table_input.ImportTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.import_table_output.ImportTableOutput, zapros.Response
]:
    raise NotImplementedError("operationContextParams JMESPath not yet supported")
