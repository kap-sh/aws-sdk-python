"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcTenancy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_vpc_tenancy_request
    import aws_sdk_ec2.types.modify_vpc_tenancy_result


def modify_vpc_tenancy(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_tenancy_request.ModifyVpcTenancyRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_tenancy_result.ModifyVpcTenancyResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_vpc_tenancy(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_tenancy_request.ModifyVpcTenancyRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_tenancy_result.ModifyVpcTenancyResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
