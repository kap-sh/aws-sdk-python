"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumeAttribute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_volume_attribute_request
    import aws_sdk_ec2.types.describe_volume_attribute_result


def describe_volume_attribute(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_volume_attribute_request.DescribeVolumeAttributeRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_volume_attribute_result.DescribeVolumeAttributeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_volume_attribute(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_volume_attribute_request.DescribeVolumeAttributeRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_volume_attribute_result.DescribeVolumeAttributeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
