"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReports``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_image_usage_reports_request
    import aws_sdk_ec2.types.describe_image_usage_reports_result


def describe_image_usage_reports(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_image_usage_reports_request.DescribeImageUsageReportsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_image_usage_reports_result.DescribeImageUsageReportsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_image_usage_reports(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_image_usage_reports_request.DescribeImageUsageReportsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_image_usage_reports_result.DescribeImageUsageReportsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
