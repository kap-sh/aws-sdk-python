"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSubnetCidrBlock``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_subnet_cidr_block_request
    import aws_sdk_ec2.types.disassociate_subnet_cidr_block_result


def disassociate_subnet_cidr_block(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_subnet_cidr_block_request.DisassociateSubnetCidrBlockRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_subnet_cidr_block_result.DisassociateSubnetCidrBlockResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_subnet_cidr_block(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_subnet_cidr_block_request.DisassociateSubnetCidrBlockRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_subnet_cidr_block_result.DisassociateSubnetCidrBlockResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
