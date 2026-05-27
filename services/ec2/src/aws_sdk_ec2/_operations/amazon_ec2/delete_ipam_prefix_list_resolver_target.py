"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPrefixListResolverTarget``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_request
    import aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_result


def delete_ipam_prefix_list_resolver_target(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_request.DeleteIpamPrefixListResolverTargetRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_result.DeleteIpamPrefixListResolverTargetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_ipam_prefix_list_resolver_target(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_request.DeleteIpamPrefixListResolverTargetRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_result.DeleteIpamPrefixListResolverTargetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
