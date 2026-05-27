"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreManagedPrefixListVersion``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.restore_managed_prefix_list_version_request
    import aws_sdk_ec2.types.restore_managed_prefix_list_version_result


def restore_managed_prefix_list_version(
    options: OperationOptions,
    input: aws_sdk_ec2.types.restore_managed_prefix_list_version_request.RestoreManagedPrefixListVersionRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_managed_prefix_list_version_result.RestoreManagedPrefixListVersionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_restore_managed_prefix_list_version(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.restore_managed_prefix_list_version_request.RestoreManagedPrefixListVersionRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_managed_prefix_list_version_result.RestoreManagedPrefixListVersionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
