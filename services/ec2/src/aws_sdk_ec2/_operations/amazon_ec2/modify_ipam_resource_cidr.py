"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_ipam_resource_cidr_request
    import aws_sdk_ec2.types.modify_ipam_resource_cidr_result


def modify_ipam_resource_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_ipam_resource_cidr_request.ModifyIpamResourceCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_ipam_resource_cidr_result.ModifyIpamResourceCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_ipam_resource_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_ipam_resource_cidr_request.ModifyIpamResourceCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_ipam_resource_cidr_result.ModifyIpamResourceCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
