"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAllowedImagesSettings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_allowed_images_settings_request
    import aws_sdk_ec2.types.enable_allowed_images_settings_result


def enable_allowed_images_settings(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_allowed_images_settings_request.EnableAllowedImagesSettingsRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_allowed_images_settings_result.EnableAllowedImagesSettingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_allowed_images_settings(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_allowed_images_settings_request.EnableAllowedImagesSettingsRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_allowed_images_settings_result.EnableAllowedImagesSettingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
