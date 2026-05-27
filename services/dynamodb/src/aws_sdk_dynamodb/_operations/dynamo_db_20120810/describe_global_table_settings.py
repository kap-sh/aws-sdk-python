"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableSettings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_global_table_settings_input
    import aws_sdk_dynamodb.types.describe_global_table_settings_output


def describe_global_table_settings(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_global_table_settings_input.DescribeGlobalTableSettingsInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_global_table_settings_output.DescribeGlobalTableSettingsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_global_table_settings(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_global_table_settings_input.DescribeGlobalTableSettingsInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_global_table_settings_output.DescribeGlobalTableSettingsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
