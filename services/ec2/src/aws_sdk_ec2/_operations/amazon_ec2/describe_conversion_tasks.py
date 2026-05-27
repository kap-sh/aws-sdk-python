"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTasks``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_conversion_tasks_request
    import aws_sdk_ec2.types.describe_conversion_tasks_result


def describe_conversion_tasks(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_conversion_tasks_request.DescribeConversionTasksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_conversion_tasks_result.DescribeConversionTasksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_conversion_tasks(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_conversion_tasks_request.DescribeConversionTasksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_conversion_tasks_result.DescribeConversionTasksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
