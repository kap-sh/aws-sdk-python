"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReportEntries``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_image_usage_report_entries_request
    import aws_sdk_ec2.types.describe_image_usage_report_entries_result


def describe_image_usage_report_entries(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_image_usage_report_entries_request.DescribeImageUsageReportEntriesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_image_usage_report_entries_result.DescribeImageUsageReportEntriesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_image_usage_report_entries(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_image_usage_report_entries_request.DescribeImageUsageReportEntriesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_image_usage_report_entries_result.DescribeImageUsageReportEntriesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
