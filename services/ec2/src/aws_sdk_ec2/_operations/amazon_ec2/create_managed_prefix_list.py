"""Generated from Smithy shape ``com.amazonaws.ec2#CreateManagedPrefixList``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_managed_prefix_list_request
    import aws_sdk_ec2.types.create_managed_prefix_list_result


def create_managed_prefix_list(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_managed_prefix_list_request.CreateManagedPrefixListRequest,
) -> tuple[
    aws_sdk_ec2.types.create_managed_prefix_list_result.CreateManagedPrefixListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_managed_prefix_list(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_managed_prefix_list_request.CreateManagedPrefixListRequest,
) -> tuple[
    aws_sdk_ec2.types.create_managed_prefix_list_result.CreateManagedPrefixListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
