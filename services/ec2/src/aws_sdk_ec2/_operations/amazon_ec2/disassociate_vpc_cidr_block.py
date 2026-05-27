"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateVpcCidrBlock``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_vpc_cidr_block_request
    import aws_sdk_ec2.types.disassociate_vpc_cidr_block_result


def disassociate_vpc_cidr_block(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_vpc_cidr_block_request.DisassociateVpcCidrBlockRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_vpc_cidr_block_result.DisassociateVpcCidrBlockResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_vpc_cidr_block(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_vpc_cidr_block_request.DisassociateVpcCidrBlockRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_vpc_cidr_block_result.DisassociateVpcCidrBlockResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
