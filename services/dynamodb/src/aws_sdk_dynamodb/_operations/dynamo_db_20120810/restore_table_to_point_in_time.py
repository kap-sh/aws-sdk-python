"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableToPointInTime``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.restore_table_to_point_in_time_input
    import aws_sdk_dynamodb.types.restore_table_to_point_in_time_output


def restore_table_to_point_in_time(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.restore_table_to_point_in_time_input.RestoreTableToPointInTimeInput,
) -> tuple[
    aws_sdk_dynamodb.types.restore_table_to_point_in_time_output.RestoreTableToPointInTimeOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_restore_table_to_point_in_time(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.restore_table_to_point_in_time_input.RestoreTableToPointInTimeInput,
) -> tuple[
    aws_sdk_dynamodb.types.restore_table_to_point_in_time_output.RestoreTableToPointInTimeOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
