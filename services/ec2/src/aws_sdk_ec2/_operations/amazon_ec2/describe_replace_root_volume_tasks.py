"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReplaceRootVolumeTasks``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_replace_root_volume_tasks_request
    import aws_sdk_ec2.types.describe_replace_root_volume_tasks_result


def describe_replace_root_volume_tasks(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_replace_root_volume_tasks_request.DescribeReplaceRootVolumeTasksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_replace_root_volume_tasks_result.DescribeReplaceRootVolumeTasksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_replace_root_volume_tasks(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_replace_root_volume_tasks_request.DescribeReplaceRootVolumeTasksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_replace_root_volume_tasks_result.DescribeReplaceRootVolumeTasksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
