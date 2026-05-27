"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_volumes_request
    import aws_sdk_ec2.types.describe_volumes_result


def describe_volumes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_volumes_request.DescribeVolumesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_volumes_result.DescribeVolumesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_volumes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_volumes_request.DescribeVolumesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_volumes_result.DescribeVolumesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
