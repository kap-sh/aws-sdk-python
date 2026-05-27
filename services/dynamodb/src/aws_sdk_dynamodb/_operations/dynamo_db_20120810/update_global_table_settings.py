"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableSettings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.update_global_table_settings_input
    import aws_sdk_dynamodb.types.update_global_table_settings_output


def update_global_table_settings(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.update_global_table_settings_input.UpdateGlobalTableSettingsInput,
) -> tuple[
    aws_sdk_dynamodb.types.update_global_table_settings_output.UpdateGlobalTableSettingsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_global_table_settings(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.update_global_table_settings_input.UpdateGlobalTableSettingsInput,
) -> tuple[
    aws_sdk_dynamodb.types.update_global_table_settings_output.UpdateGlobalTableSettingsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
