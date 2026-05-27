"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportTableToPointInTime``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_table_to_point_in_time_input
    import aws_sdk_dynamodb.types.export_table_to_point_in_time_output


def export_table_to_point_in_time(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.export_table_to_point_in_time_input.ExportTableToPointInTimeInput,
) -> tuple[
    aws_sdk_dynamodb.types.export_table_to_point_in_time_output.ExportTableToPointInTimeOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_export_table_to_point_in_time(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.export_table_to_point_in_time_input.ExportTableToPointInTimeInput,
) -> tuple[
    aws_sdk_dynamodb.types.export_table_to_point_in_time_output.ExportTableToPointInTimeOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
