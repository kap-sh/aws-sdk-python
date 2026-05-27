"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAccountAttributes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_account_attributes_request
    import aws_sdk_ec2.types.describe_account_attributes_result


def describe_account_attributes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_account_attributes_request.DescribeAccountAttributesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_account_attributes_result.DescribeAccountAttributesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_account_attributes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_account_attributes_request.DescribeAccountAttributesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_account_attributes_result.DescribeAccountAttributesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
