"""Generated from Smithy shape ``com.amazonaws.ec2#DisableImageDeprecation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_image_deprecation_request
    import aws_sdk_ec2.types.disable_image_deprecation_result


def disable_image_deprecation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_image_deprecation_request.DisableImageDeprecationRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_image_deprecation_result.DisableImageDeprecationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_image_deprecation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_image_deprecation_request.DisableImageDeprecationRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_image_deprecation_result.DisableImageDeprecationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
