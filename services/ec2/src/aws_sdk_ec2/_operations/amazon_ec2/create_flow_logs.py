"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFlowLogs``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_flow_logs_request
    import aws_sdk_ec2.types.create_flow_logs_result


def create_flow_logs(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_flow_logs_request.CreateFlowLogsRequest,
) -> tuple[
    aws_sdk_ec2.types.create_flow_logs_result.CreateFlowLogsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_flow_logs(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_flow_logs_request.CreateFlowLogsRequest,
) -> tuple[
    aws_sdk_ec2.types.create_flow_logs_result.CreateFlowLogsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
