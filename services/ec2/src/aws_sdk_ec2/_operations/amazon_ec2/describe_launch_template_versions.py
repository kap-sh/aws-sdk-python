"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplateVersions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_launch_template_versions_request
    import aws_sdk_ec2.types.describe_launch_template_versions_result


def describe_launch_template_versions(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_launch_template_versions_request.DescribeLaunchTemplateVersionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_launch_template_versions_result.DescribeLaunchTemplateVersionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_launch_template_versions(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_launch_template_versions_request.DescribeLaunchTemplateVersionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_launch_template_versions_result.DescribeLaunchTemplateVersionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
