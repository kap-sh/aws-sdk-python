"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListGlobalTables``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_global_tables_input
    import aws_sdk_dynamodb.types.list_global_tables_output


def list_global_tables(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.list_global_tables_input.ListGlobalTablesInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_global_tables_output.ListGlobalTablesOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_global_tables(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.list_global_tables_input.ListGlobalTablesInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_global_tables_output.ListGlobalTablesOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
