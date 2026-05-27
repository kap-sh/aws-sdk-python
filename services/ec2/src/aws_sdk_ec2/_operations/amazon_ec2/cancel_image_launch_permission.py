"""Generated from Smithy shape ``com.amazonaws.ec2#CancelImageLaunchPermission``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_image_launch_permission_request
    import aws_sdk_ec2.types.cancel_image_launch_permission_result


def cancel_image_launch_permission(
    options: OperationOptions,
    input: aws_sdk_ec2.types.cancel_image_launch_permission_request.CancelImageLaunchPermissionRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_image_launch_permission_result.CancelImageLaunchPermissionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_image_launch_permission(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.cancel_image_launch_permission_request.CancelImageLaunchPermissionRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_image_launch_permission_result.CancelImageLaunchPermissionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
