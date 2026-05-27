"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterImage``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.deregister_image_request
    import aws_sdk_ec2.types.deregister_image_result


def deregister_image(
    options: OperationOptions,
    input: aws_sdk_ec2.types.deregister_image_request.DeregisterImageRequest,
) -> tuple[
    aws_sdk_ec2.types.deregister_image_result.DeregisterImageResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_deregister_image(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.deregister_image_request.DeregisterImageRequest,
) -> tuple[
    aws_sdk_ec2.types.deregister_image_result.DeregisterImageResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
