"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImages``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_launch_images_request
    import aws_sdk_ec2.types.describe_fast_launch_images_result


def describe_fast_launch_images(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_fast_launch_images_request.DescribeFastLaunchImagesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fast_launch_images_result.DescribeFastLaunchImagesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_fast_launch_images(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_fast_launch_images_request.DescribeFastLaunchImagesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fast_launch_images_result.DescribeFastLaunchImagesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
