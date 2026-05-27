"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedPrefixList``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_managed_prefix_list_request
    import aws_sdk_ec2.types.modify_managed_prefix_list_result


def modify_managed_prefix_list(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_managed_prefix_list_request.ModifyManagedPrefixListRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_managed_prefix_list_result.ModifyManagedPrefixListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_managed_prefix_list(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_managed_prefix_list_request.ModifyManagedPrefixListRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_managed_prefix_list_result.ModifyManagedPrefixListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
