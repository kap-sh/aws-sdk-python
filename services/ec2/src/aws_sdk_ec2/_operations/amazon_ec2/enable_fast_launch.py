"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastLaunch``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_launch_request
    import aws_sdk_ec2.types.enable_fast_launch_result


def enable_fast_launch(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_fast_launch_request.EnableFastLaunchRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_fast_launch_result.EnableFastLaunchResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_fast_launch(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_fast_launch_request.EnableFastLaunchRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_fast_launch_result.EnableFastLaunchResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
