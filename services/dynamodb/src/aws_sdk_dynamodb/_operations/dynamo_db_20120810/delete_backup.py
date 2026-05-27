"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteBackup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.delete_backup_input
    import aws_sdk_dynamodb.types.delete_backup_output


def delete_backup(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.delete_backup_input.DeleteBackupInput,
) -> tuple[
    aws_sdk_dynamodb.types.delete_backup_output.DeleteBackupOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_backup(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.delete_backup_input.DeleteBackupInput,
) -> tuple[
    aws_sdk_dynamodb.types.delete_backup_output.DeleteBackupOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
