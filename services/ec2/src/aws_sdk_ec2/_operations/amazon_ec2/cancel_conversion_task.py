"""Generated from Smithy shape ``com.amazonaws.ec2#CancelConversionTask``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_conversion_request


def cancel_conversion_task(
    options: OperationOptions,
    input: aws_sdk_ec2.types.cancel_conversion_request.CancelConversionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_conversion_task(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.cancel_conversion_request.CancelConversionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
