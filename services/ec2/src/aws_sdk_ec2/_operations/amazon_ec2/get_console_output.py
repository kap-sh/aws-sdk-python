"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleOutput``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_console_output_request
    import aws_sdk_ec2.types.get_console_output_result


def get_console_output(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_console_output_request.GetConsoleOutputRequest,
) -> tuple[
    aws_sdk_ec2.types.get_console_output_result.GetConsoleOutputResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_console_output(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_console_output_request.GetConsoleOutputRequest,
) -> tuple[
    aws_sdk_ec2.types.get_console_output_result.GetConsoleOutputResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
