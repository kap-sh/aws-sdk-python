"""Generated from Smithy shape ``com.amazonaws.ec2#DisableImageDeregistrationProtection``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_image_deregistration_protection_request
    import aws_sdk_ec2.types.disable_image_deregistration_protection_result


def disable_image_deregistration_protection(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_image_deregistration_protection_request.DisableImageDeregistrationProtectionRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_image_deregistration_protection_result.DisableImageDeregistrationProtectionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_image_deregistration_protection(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_image_deregistration_protection_request.DisableImageDeregistrationProtectionRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_image_deregistration_protection_result.DisableImageDeregistrationProtectionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
