"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTable``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_global_table_input
    import aws_sdk_dynamodb.types.describe_global_table_output


def describe_global_table(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_global_table_input.DescribeGlobalTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_global_table_output.DescribeGlobalTableOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_global_table(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_global_table_input.DescribeGlobalTableInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_global_table_output.DescribeGlobalTableOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
