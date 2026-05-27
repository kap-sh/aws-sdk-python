"""Generated from Smithy shape ``com.amazonaws.ec2#DisableSerialConsoleAccess``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_serial_console_access_request
    import aws_sdk_ec2.types.disable_serial_console_access_result


def disable_serial_console_access(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_serial_console_access_request.DisableSerialConsoleAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_serial_console_access_result.DisableSerialConsoleAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_serial_console_access(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_serial_console_access_request.DisableSerialConsoleAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_serial_console_access_result.DisableSerialConsoleAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
