"""Generated from Smithy shape ``com.amazonaws.ec2#DisableImageBlockPublicAccess``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_image_block_public_access_request
    import aws_sdk_ec2.types.disable_image_block_public_access_result


def disable_image_block_public_access(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_image_block_public_access_request.DisableImageBlockPublicAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_image_block_public_access_result.DisableImageBlockPublicAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_image_block_public_access(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_image_block_public_access_request.DisableImageBlockPublicAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_image_block_public_access_result.DisableImageBlockPublicAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
