"""Generated from Smithy shape ``com.amazonaws.ec2#EnableSerialConsoleAccess``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_serial_console_access_request
    import aws_sdk_ec2.types.enable_serial_console_access_result


def enable_serial_console_access(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_serial_console_access_request.EnableSerialConsoleAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_serial_console_access_result.EnableSerialConsoleAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_serial_console_access(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_serial_console_access_request.EnableSerialConsoleAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_serial_console_access_result.EnableSerialConsoleAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
