"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteStatement``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.execute_statement_input
    import aws_sdk_dynamodb.types.execute_statement_output


def execute_statement(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.execute_statement_input.ExecuteStatementInput,
) -> tuple[
    aws_sdk_dynamodb.types.execute_statement_output.ExecuteStatementOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_execute_statement(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.execute_statement_input.ExecuteStatementInput,
) -> tuple[
    aws_sdk_dynamodb.types.execute_statement_output.ExecuteStatementOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
