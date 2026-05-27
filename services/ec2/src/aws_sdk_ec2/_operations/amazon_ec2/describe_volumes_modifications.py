"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesModifications``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_volumes_modifications_request
    import aws_sdk_ec2.types.describe_volumes_modifications_result


def describe_volumes_modifications(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_volumes_modifications_request.DescribeVolumesModificationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_volumes_modifications_result.DescribeVolumesModificationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_volumes_modifications(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_volumes_modifications_request.DescribeVolumesModificationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_volumes_modifications_result.DescribeVolumesModificationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
