"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTail``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_cloudwatch_logs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.start_live_tail_request
    import aws_sdk_cloudwatch_logs.types.start_live_tail_response


def start_live_tail(
    options: OperationOptions,
    input: aws_sdk_cloudwatch_logs.types.start_live_tail_request.StartLiveTailRequest,
) -> tuple[
    aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_start_live_tail(
    options: AsyncOperationOptions,
    input: aws_sdk_cloudwatch_logs.types.start_live_tail_request.StartLiveTailRequest,
) -> tuple[
    aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
