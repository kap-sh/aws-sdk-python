"""Generated from Smithy shape ``com.amazonaws.ec2#DeletePublicIpv4Pool``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_public_ipv4_pool_request
    import aws_sdk_ec2.types.delete_public_ipv4_pool_result


def delete_public_ipv4_pool(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_public_ipv4_pool_request.DeletePublicIpv4PoolRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_public_ipv4_pool_result.DeletePublicIpv4PoolResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_public_ipv4_pool(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_public_ipv4_pool_request.DeletePublicIpv4PoolRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_public_ipv4_pool_result.DeletePublicIpv4PoolResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
