"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeExport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_export_input
    import aws_sdk_dynamodb.types.describe_export_output


def describe_export(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_export_input.DescribeExportInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_export_output.DescribeExportOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_export(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_export_input.DescribeExportInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_export_output.DescribeExportOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
