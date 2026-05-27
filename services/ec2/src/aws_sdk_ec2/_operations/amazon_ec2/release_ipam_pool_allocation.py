"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseIpamPoolAllocation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.release_ipam_pool_allocation_request
    import aws_sdk_ec2.types.release_ipam_pool_allocation_result


def release_ipam_pool_allocation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.release_ipam_pool_allocation_request.ReleaseIpamPoolAllocationRequest,
) -> tuple[
    aws_sdk_ec2.types.release_ipam_pool_allocation_result.ReleaseIpamPoolAllocationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_release_ipam_pool_allocation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.release_ipam_pool_allocation_request.ReleaseIpamPoolAllocationRequest,
) -> tuple[
    aws_sdk_ec2.types.release_ipam_pool_allocation_result.ReleaseIpamPoolAllocationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
