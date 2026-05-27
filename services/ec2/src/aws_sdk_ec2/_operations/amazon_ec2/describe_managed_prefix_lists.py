"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeManagedPrefixLists``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_managed_prefix_lists_request
    import aws_sdk_ec2.types.describe_managed_prefix_lists_result


def describe_managed_prefix_lists(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_managed_prefix_lists_request.DescribeManagedPrefixListsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_managed_prefix_lists_result.DescribeManagedPrefixListsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_managed_prefix_lists(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_managed_prefix_lists_request.DescribeManagedPrefixListsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_managed_prefix_lists_result.DescribeManagedPrefixListsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
