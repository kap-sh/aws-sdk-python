"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageBlockPublicAccessState``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_image_block_public_access_state_request
    import aws_sdk_ec2.types.get_image_block_public_access_state_result


def get_image_block_public_access_state(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_image_block_public_access_state_request.GetImageBlockPublicAccessStateRequest,
) -> tuple[
    aws_sdk_ec2.types.get_image_block_public_access_state_result.GetImageBlockPublicAccessStateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_image_block_public_access_state(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_image_block_public_access_state_request.GetImageBlockPublicAccessStateRequest,
) -> tuple[
    aws_sdk_ec2.types.get_image_block_public_access_state_result.GetImageBlockPublicAccessStateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
