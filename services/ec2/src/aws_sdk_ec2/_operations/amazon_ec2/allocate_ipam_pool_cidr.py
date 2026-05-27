"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateIpamPoolCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocate_ipam_pool_cidr_request
    import aws_sdk_ec2.types.allocate_ipam_pool_cidr_result


def allocate_ipam_pool_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.allocate_ipam_pool_cidr_request.AllocateIpamPoolCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.allocate_ipam_pool_cidr_result.AllocateIpamPoolCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_allocate_ipam_pool_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.allocate_ipam_pool_cidr_request.AllocateIpamPoolCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.allocate_ipam_pool_cidr_result.AllocateIpamPoolCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
