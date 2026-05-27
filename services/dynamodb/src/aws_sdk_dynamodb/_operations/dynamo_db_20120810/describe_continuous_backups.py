"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContinuousBackups``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_continuous_backups_input
    import aws_sdk_dynamodb.types.describe_continuous_backups_output


def describe_continuous_backups(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_continuous_backups_input.DescribeContinuousBackupsInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_continuous_backups_output.DescribeContinuousBackupsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_continuous_backups(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_continuous_backups_input.DescribeContinuousBackupsInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_continuous_backups_output.DescribeContinuousBackupsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
