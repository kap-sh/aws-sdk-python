"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceImageCriteriaInAllowedImagesSettings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_request
    import aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_result


def replace_image_criteria_in_allowed_images_settings(
    options: OperationOptions,
    input: aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_request.ReplaceImageCriteriaInAllowedImagesSettingsRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_result.ReplaceImageCriteriaInAllowedImagesSettingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_replace_image_criteria_in_allowed_images_settings(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_request.ReplaceImageCriteriaInAllowedImagesSettingsRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_result.ReplaceImageCriteriaInAllowedImagesSettingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
