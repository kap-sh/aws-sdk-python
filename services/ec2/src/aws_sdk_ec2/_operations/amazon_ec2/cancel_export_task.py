"""Generated from Smithy shape ``com.amazonaws.ec2#CancelExportTask``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_export_task_request


def cancel_export_task(
    options: OperationOptions,
    input: aws_sdk_ec2.types.cancel_export_task_request.CancelExportTaskRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_export_task(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.cancel_export_task_request.CancelExportTaskRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
