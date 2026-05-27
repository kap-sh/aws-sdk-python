"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeBundleTasks``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_bundle_tasks_request
    import aws_sdk_ec2.types.describe_bundle_tasks_result


def describe_bundle_tasks(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_bundle_tasks_request.DescribeBundleTasksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_bundle_tasks_result.DescribeBundleTasksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_bundle_tasks(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_bundle_tasks_request.DescribeBundleTasksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_bundle_tasks_result.DescribeBundleTasksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
