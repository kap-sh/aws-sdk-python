"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteImageUsageReport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_image_usage_report_request
    import aws_sdk_ec2.types.delete_image_usage_report_result


def delete_image_usage_report(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_image_usage_report_request.DeleteImageUsageReportRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_image_usage_report_result.DeleteImageUsageReportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_image_usage_report(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_image_usage_report_request.DeleteImageUsageReportRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_image_usage_report_result.DeleteImageUsageReportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
