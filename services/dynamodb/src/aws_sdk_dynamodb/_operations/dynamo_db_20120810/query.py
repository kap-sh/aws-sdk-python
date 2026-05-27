"""Generated from Smithy shape ``com.amazonaws.dynamodb#Query``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.query_input
    import aws_sdk_dynamodb.types.query_output


def query(
    options: OperationOptions, input: aws_sdk_dynamodb.types.query_input.QueryInput
) -> tuple[aws_sdk_dynamodb.types.query_output.QueryOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_query(
    options: AsyncOperationOptions, input: aws_sdk_dynamodb.types.query_input.QueryInput
) -> tuple[aws_sdk_dynamodb.types.query_output.QueryOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
