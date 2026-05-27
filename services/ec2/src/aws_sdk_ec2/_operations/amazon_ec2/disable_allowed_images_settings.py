"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAllowedImagesSettings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_allowed_images_settings_request
    import aws_sdk_ec2.types.disable_allowed_images_settings_result


def disable_allowed_images_settings(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_allowed_images_settings_request.DisableAllowedImagesSettingsRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_allowed_images_settings_result.DisableAllowedImagesSettingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_allowed_images_settings(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_allowed_images_settings_request.DisableAllowedImagesSettingsRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_allowed_images_settings_result.DisableAllowedImagesSettingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
