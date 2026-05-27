"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPrefixListResolverTarget``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_request
    import aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_result


def modify_ipam_prefix_list_resolver_target(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_request.ModifyIpamPrefixListResolverTargetRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_result.ModifyIpamPrefixListResolverTargetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_ipam_prefix_list_resolver_target(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_request.ModifyIpamPrefixListResolverTargetRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_result.ModifyIpamPrefixListResolverTargetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
