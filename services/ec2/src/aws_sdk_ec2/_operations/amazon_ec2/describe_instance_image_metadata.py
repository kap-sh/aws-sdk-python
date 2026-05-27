"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceImageMetadata``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_instance_image_metadata_request
    import aws_sdk_ec2.types.describe_instance_image_metadata_result


def describe_instance_image_metadata(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_instance_image_metadata_request.DescribeInstanceImageMetadataRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_image_metadata_result.DescribeInstanceImageMetadataResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_instance_image_metadata(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_instance_image_metadata_request.DescribeInstanceImageMetadataRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_image_metadata_result.DescribeInstanceImageMetadataResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
