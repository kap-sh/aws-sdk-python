"""Generated from Smithy shape ``com.amazonaws.ec2#GetSecurityGroupsForVpc``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_security_groups_for_vpc_request
    import aws_sdk_ec2.types.get_security_groups_for_vpc_result


def get_security_groups_for_vpc(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_security_groups_for_vpc_request.GetSecurityGroupsForVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.get_security_groups_for_vpc_result.GetSecurityGroupsForVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_security_groups_for_vpc(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_security_groups_for_vpc_request.GetSecurityGroupsForVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.get_security_groups_for_vpc_result.GetSecurityGroupsForVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
