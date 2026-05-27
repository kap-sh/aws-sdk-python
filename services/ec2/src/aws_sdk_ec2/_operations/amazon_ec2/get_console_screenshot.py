"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleScreenshot``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_console_screenshot_request
    import aws_sdk_ec2.types.get_console_screenshot_result


def get_console_screenshot(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_console_screenshot_request.GetConsoleScreenshotRequest,
) -> tuple[
    aws_sdk_ec2.types.get_console_screenshot_result.GetConsoleScreenshotResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_console_screenshot(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_console_screenshot_request.GetConsoleScreenshotRequest,
) -> tuple[
    aws_sdk_ec2.types.get_console_screenshot_result.GetConsoleScreenshotResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
