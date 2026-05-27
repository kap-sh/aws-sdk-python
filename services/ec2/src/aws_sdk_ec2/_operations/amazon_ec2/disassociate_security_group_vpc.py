"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSecurityGroupVpc``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_security_group_vpc_request
    import aws_sdk_ec2.types.disassociate_security_group_vpc_result


def disassociate_security_group_vpc(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_security_group_vpc_request.DisassociateSecurityGroupVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_security_group_vpc_result.DisassociateSecurityGroupVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_security_group_vpc(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_security_group_vpc_request.DisassociateSecurityGroupVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_security_group_vpc_result.DisassociateSecurityGroupVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
