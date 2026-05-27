"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPoolCidrs``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ipam_pool_cidrs_request
    import aws_sdk_ec2.types.get_ipam_pool_cidrs_result


def get_ipam_pool_cidrs(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ipam_pool_cidrs_request.GetIpamPoolCidrsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_pool_cidrs_result.GetIpamPoolCidrsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ipam_pool_cidrs(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ipam_pool_cidrs_request.GetIpamPoolCidrsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_pool_cidrs_result.GetIpamPoolCidrsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
