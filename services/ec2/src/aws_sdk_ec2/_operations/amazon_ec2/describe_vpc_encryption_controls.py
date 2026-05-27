"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEncryptionControls``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_vpc_encryption_controls_request
    import aws_sdk_ec2.types.describe_vpc_encryption_controls_result


def describe_vpc_encryption_controls(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_vpc_encryption_controls_request.DescribeVpcEncryptionControlsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpc_encryption_controls_result.DescribeVpcEncryptionControlsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_vpc_encryption_controls(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_vpc_encryption_controls_request.DescribeVpcEncryptionControlsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpc_encryption_controls_result.DescribeVpcEncryptionControlsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
