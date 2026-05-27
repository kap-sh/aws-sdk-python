"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedPrefixListAssociations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_managed_prefix_list_associations_request
    import aws_sdk_ec2.types.get_managed_prefix_list_associations_result


def get_managed_prefix_list_associations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_managed_prefix_list_associations_request.GetManagedPrefixListAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_managed_prefix_list_associations_result.GetManagedPrefixListAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_managed_prefix_list_associations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_managed_prefix_list_associations_request.GetManagedPrefixListAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_managed_prefix_list_associations_result.GetManagedPrefixListAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
