"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignPrivateNatGatewayAddress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unassign_private_nat_gateway_address_request
    import aws_sdk_ec2.types.unassign_private_nat_gateway_address_result


def unassign_private_nat_gateway_address(
    options: OperationOptions,
    input: aws_sdk_ec2.types.unassign_private_nat_gateway_address_request.UnassignPrivateNatGatewayAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.unassign_private_nat_gateway_address_result.UnassignPrivateNatGatewayAddressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_unassign_private_nat_gateway_address(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.unassign_private_nat_gateway_address_request.UnassignPrivateNatGatewayAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.unassign_private_nat_gateway_address_result.UnassignPrivateNatGatewayAddressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
