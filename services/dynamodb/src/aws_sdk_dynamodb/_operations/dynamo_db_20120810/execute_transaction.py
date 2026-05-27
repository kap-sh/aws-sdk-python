"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteTransaction``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.execute_transaction_input
    import aws_sdk_dynamodb.types.execute_transaction_output


def execute_transaction(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.execute_transaction_input.ExecuteTransactionInput,
) -> tuple[
    aws_sdk_dynamodb.types.execute_transaction_output.ExecuteTransactionOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_execute_transaction(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.execute_transaction_input.ExecuteTransactionInput,
) -> tuple[
    aws_sdk_dynamodb.types.execute_transaction_output.ExecuteTransactionOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
