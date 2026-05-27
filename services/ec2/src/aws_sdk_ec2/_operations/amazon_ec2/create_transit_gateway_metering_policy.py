"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMeteringPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_transit_gateway_metering_policy_request
    import aws_sdk_ec2.types.create_transit_gateway_metering_policy_result


def create_transit_gateway_metering_policy(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_transit_gateway_metering_policy_request.CreateTransitGatewayMeteringPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.create_transit_gateway_metering_policy_result.CreateTransitGatewayMeteringPolicyResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_transit_gateway_metering_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_transit_gateway_metering_policy_request.CreateTransitGatewayMeteringPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.create_transit_gateway_metering_policy_result.CreateTransitGatewayMeteringPolicyResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
