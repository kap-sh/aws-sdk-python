"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListBackups``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_backups_input
    import aws_sdk_dynamodb.types.list_backups_output


def list_backups(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.list_backups_input.ListBackupsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_backups_output.ListBackupsOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_backups(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.list_backups_input.ListBackupsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_backups_output.ListBackupsOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
