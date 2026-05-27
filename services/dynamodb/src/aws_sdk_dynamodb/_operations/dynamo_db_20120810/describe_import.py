"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeImport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_import_input
    import aws_sdk_dynamodb.types.describe_import_output


def describe_import(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_import_input.DescribeImportInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_import_output.DescribeImportOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_import(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_import_input.DescribeImportInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_import_output.DescribeImportOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
