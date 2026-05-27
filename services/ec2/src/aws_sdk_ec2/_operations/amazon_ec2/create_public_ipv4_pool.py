"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePublicIpv4Pool``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_public_ipv4_pool_request
    import aws_sdk_ec2.types.create_public_ipv4_pool_result


def create_public_ipv4_pool(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_public_ipv4_pool_request.CreatePublicIpv4PoolRequest,
) -> tuple[
    aws_sdk_ec2.types.create_public_ipv4_pool_result.CreatePublicIpv4PoolResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_public_ipv4_pool(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_public_ipv4_pool_request.CreatePublicIpv4PoolRequest,
) -> tuple[
    aws_sdk_ec2.types.create_public_ipv4_pool_result.CreatePublicIpv4PoolResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
