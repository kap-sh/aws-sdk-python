"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessGroups``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_verified_access_groups_request
    import aws_sdk_ec2.types.describe_verified_access_groups_result


def describe_verified_access_groups(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_verified_access_groups_request.DescribeVerifiedAccessGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_verified_access_groups_result.DescribeVerifiedAccessGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_verified_access_groups(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_verified_access_groups_request.DescribeVerifiedAccessGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_verified_access_groups_result.DescribeVerifiedAccessGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
