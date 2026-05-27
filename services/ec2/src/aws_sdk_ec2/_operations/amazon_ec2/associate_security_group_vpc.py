"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateSecurityGroupVpc``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_security_group_vpc_request
    import aws_sdk_ec2.types.associate_security_group_vpc_result


def associate_security_group_vpc(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_security_group_vpc_request.AssociateSecurityGroupVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_security_group_vpc_result.AssociateSecurityGroupVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_security_group_vpc(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_security_group_vpc_request.AssociateSecurityGroupVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_security_group_vpc_result.AssociateSecurityGroupVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
