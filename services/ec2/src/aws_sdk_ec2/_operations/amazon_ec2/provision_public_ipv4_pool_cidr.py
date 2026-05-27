"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionPublicIpv4PoolCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_request
    import aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_result


def provision_public_ipv4_pool_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_request.ProvisionPublicIpv4PoolCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_result.ProvisionPublicIpv4PoolCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_provision_public_ipv4_pool_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_request.ProvisionPublicIpv4PoolCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_result.ProvisionPublicIpv4PoolCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
