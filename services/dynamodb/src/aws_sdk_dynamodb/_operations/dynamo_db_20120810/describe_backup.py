"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeBackup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_backup_input
    import aws_sdk_dynamodb.types.describe_backup_output


def describe_backup(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_backup_input.DescribeBackupInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_backup_output.DescribeBackupOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_backup(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_backup_input.DescribeBackupInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_backup_output.DescribeBackupOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
