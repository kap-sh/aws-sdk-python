"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpc``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_vpc_request


def delete_vpc(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_request.DeleteVpcRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_vpc(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_request.DeleteVpcRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
