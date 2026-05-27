"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTags``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_tags_request
    import aws_sdk_ec2.types.describe_tags_result


def describe_tags(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_tags_request.DescribeTagsRequest,
) -> tuple[aws_sdk_ec2.types.describe_tags_result.DescribeTagsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_tags(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_tags_request.DescribeTagsRequest,
) -> tuple[aws_sdk_ec2.types.describe_tags_result.DescribeTagsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
