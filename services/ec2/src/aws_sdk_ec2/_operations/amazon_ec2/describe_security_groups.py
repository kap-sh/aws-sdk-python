"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroups``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_security_groups_request
    import aws_sdk_ec2.types.describe_security_groups_result


def describe_security_groups(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_security_groups_request.DescribeSecurityGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_security_groups_result.DescribeSecurityGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_security_groups(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_security_groups_request.DescribeSecurityGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_security_groups_result.DescribeSecurityGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
