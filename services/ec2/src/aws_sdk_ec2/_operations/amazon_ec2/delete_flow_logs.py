"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFlowLogs``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_flow_logs_request
    import aws_sdk_ec2.types.delete_flow_logs_result


def delete_flow_logs(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_flow_logs_request.DeleteFlowLogsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_flow_logs_result.DeleteFlowLogsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_flow_logs(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_flow_logs_request.DeleteFlowLogsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_flow_logs_result.DeleteFlowLogsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
