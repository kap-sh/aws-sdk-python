"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalTable``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.create_global_table_input
    import aws_sdk_dynamodb.types.create_global_table_output


def create_global_table(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.create_global_table_input.CreateGlobalTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.create_global_table_output.CreateGlobalTableOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_global_table(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.create_global_table_input.CreateGlobalTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.create_global_table_output.CreateGlobalTableOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
