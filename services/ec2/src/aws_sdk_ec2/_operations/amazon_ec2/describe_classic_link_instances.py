"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClassicLinkInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_classic_link_instances_request
    import aws_sdk_ec2.types.describe_classic_link_instances_result


def describe_classic_link_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_classic_link_instances_request.DescribeClassicLinkInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_classic_link_instances_result.DescribeClassicLinkInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_classic_link_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_classic_link_instances_request.DescribeClassicLinkInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_classic_link_instances_result.DescribeClassicLinkInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
