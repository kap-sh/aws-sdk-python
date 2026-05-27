"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemon``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_daemon_request
    import aws_sdk_ecs.types.describe_daemon_response


def describe_daemon(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_daemon_request.DescribeDaemonRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_daemon_response.DescribeDaemonResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_daemon(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_daemon_request.DescribeDaemonRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_daemon_response.DescribeDaemonResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
