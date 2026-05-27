"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPoolAllocations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ipam_pool_allocations_request
    import aws_sdk_ec2.types.get_ipam_pool_allocations_result


def get_ipam_pool_allocations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ipam_pool_allocations_request.GetIpamPoolAllocationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_pool_allocations_result.GetIpamPoolAllocationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ipam_pool_allocations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ipam_pool_allocations_request.GetIpamPoolAllocationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_pool_allocations_result.GetIpamPoolAllocationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
