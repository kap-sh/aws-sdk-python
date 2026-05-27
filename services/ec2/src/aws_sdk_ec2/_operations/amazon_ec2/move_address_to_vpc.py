"""Generated from Smithy shape ``com.amazonaws.ec2#MoveAddressToVpc``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.move_address_to_vpc_request
    import aws_sdk_ec2.types.move_address_to_vpc_result


def move_address_to_vpc(
    options: OperationOptions,
    input: aws_sdk_ec2.types.move_address_to_vpc_request.MoveAddressToVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.move_address_to_vpc_result.MoveAddressToVpcResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_move_address_to_vpc(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.move_address_to_vpc_request.MoveAddressToVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.move_address_to_vpc_result.MoveAddressToVpcResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
