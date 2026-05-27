"""Generated from Smithy shape ``com.amazonaws.ec2#ListImagesInRecycleBin``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.list_images_in_recycle_bin_request
    import aws_sdk_ec2.types.list_images_in_recycle_bin_result


def list_images_in_recycle_bin(
    options: OperationOptions,
    input: aws_sdk_ec2.types.list_images_in_recycle_bin_request.ListImagesInRecycleBinRequest,
) -> tuple[
    aws_sdk_ec2.types.list_images_in_recycle_bin_result.ListImagesInRecycleBinResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_images_in_recycle_bin(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.list_images_in_recycle_bin_request.ListImagesInRecycleBinRequest,
) -> tuple[
    aws_sdk_ec2.types.list_images_in_recycle_bin_result.ListImagesInRecycleBinResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
