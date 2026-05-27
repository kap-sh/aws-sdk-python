"""Generated from Smithy shape ``com.amazonaws.ec2#GetSerialConsoleAccessStatus``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_serial_console_access_status_request
    import aws_sdk_ec2.types.get_serial_console_access_status_result


def get_serial_console_access_status(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_serial_console_access_status_request.GetSerialConsoleAccessStatusRequest,
) -> tuple[
    aws_sdk_ec2.types.get_serial_console_access_status_result.GetSerialConsoleAccessStatusResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_serial_console_access_status(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_serial_console_access_status_request.GetSerialConsoleAccessStatusRequest,
) -> tuple[
    aws_sdk_ec2.types.get_serial_console_access_status_result.GetSerialConsoleAccessStatusResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
