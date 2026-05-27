"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteManagedPrefixList``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_managed_prefix_list_request
    import aws_sdk_ec2.types.delete_managed_prefix_list_result


def delete_managed_prefix_list(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_managed_prefix_list_request.DeleteManagedPrefixListRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_managed_prefix_list_result.DeleteManagedPrefixListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_managed_prefix_list(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_managed_prefix_list_request.DeleteManagedPrefixListRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_managed_prefix_list_result.DeleteManagedPrefixListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
