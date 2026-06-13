"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObject``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
from aws_sdk_cloudwatch_logs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.get_log_object_request
    import aws_sdk_cloudwatch_logs.types.get_log_object_response


def get_log_object(
    options: OperationOptions,
    input: aws_sdk_cloudwatch_logs.types.get_log_object_request.GetLogObjectRequest,
) -> tuple[
    aws_sdk_cloudwatch_logs.types.get_log_object_response.GetLogObjectResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_get_log_object(
    options: AsyncOperationOptions,
    input: aws_sdk_cloudwatch_logs.types.get_log_object_request.GetLogObjectRequest,
) -> tuple[
    aws_sdk_cloudwatch_logs.types.get_log_object_response.GetLogObjectResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
