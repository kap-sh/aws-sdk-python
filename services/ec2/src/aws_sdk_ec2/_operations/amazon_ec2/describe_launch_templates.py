"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplates``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_launch_templates_request
    import aws_sdk_ec2.types.describe_launch_templates_result


def describe_launch_templates(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_launch_templates_request.DescribeLaunchTemplatesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_launch_templates_result.DescribeLaunchTemplatesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_launch_templates(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_launch_templates_request.DescribeLaunchTemplatesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_launch_templates_result.DescribeLaunchTemplatesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
