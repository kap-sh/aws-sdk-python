"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImage``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_image_request
    import aws_sdk_ec2.types.enable_image_result


def enable_image(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_image_request.EnableImageRequest,
) -> tuple[aws_sdk_ec2.types.enable_image_result.EnableImageResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_image(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_image_request.EnableImageRequest,
) -> tuple[aws_sdk_ec2.types.enable_image_result.EnableImageResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
