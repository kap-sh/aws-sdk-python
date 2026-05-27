"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionIpamPoolCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.deprovision_ipam_pool_cidr_request
    import aws_sdk_ec2.types.deprovision_ipam_pool_cidr_result


def deprovision_ipam_pool_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.deprovision_ipam_pool_cidr_request.DeprovisionIpamPoolCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.deprovision_ipam_pool_cidr_result.DeprovisionIpamPoolCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_deprovision_ipam_pool_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.deprovision_ipam_pool_cidr_request.DeprovisionIpamPoolCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.deprovision_ipam_pool_cidr_result.DeprovisionIpamPoolCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
