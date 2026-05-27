"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPool``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_ipam_pool_request
    import aws_sdk_ec2.types.create_ipam_pool_result


def create_ipam_pool(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_ipam_pool_request.CreateIpamPoolRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_pool_result.CreateIpamPoolResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_ipam_pool(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_ipam_pool_request.CreateIpamPoolRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_pool_result.CreateIpamPoolResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
