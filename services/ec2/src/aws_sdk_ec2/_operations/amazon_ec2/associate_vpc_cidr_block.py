"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateVpcCidrBlock``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_vpc_cidr_block_request
    import aws_sdk_ec2.types.associate_vpc_cidr_block_result


def associate_vpc_cidr_block(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_vpc_cidr_block_request.AssociateVpcCidrBlockRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_vpc_cidr_block_result.AssociateVpcCidrBlockResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_vpc_cidr_block(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_vpc_cidr_block_request.AssociateVpcCidrBlockRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_vpc_cidr_block_result.AssociateVpcCidrBlockResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
