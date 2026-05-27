"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateNatGatewayAddress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.assign_private_nat_gateway_address_request
    import aws_sdk_ec2.types.assign_private_nat_gateway_address_result


def assign_private_nat_gateway_address(
    options: OperationOptions,
    input: aws_sdk_ec2.types.assign_private_nat_gateway_address_request.AssignPrivateNatGatewayAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.assign_private_nat_gateway_address_result.AssignPrivateNatGatewayAddressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_assign_private_nat_gateway_address(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.assign_private_nat_gateway_address_request.AssignPrivateNatGatewayAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.assign_private_nat_gateway_address_result.AssignPrivateNatGatewayAddressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
