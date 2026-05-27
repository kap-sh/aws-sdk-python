"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTransitGatewayPolicyTable``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_request
    import aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_result


def disassociate_transit_gateway_policy_table(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_request.DisassociateTransitGatewayPolicyTableRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_result.DisassociateTransitGatewayPolicyTableResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_transit_gateway_policy_table(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_request.DisassociateTransitGatewayPolicyTableRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_result.DisassociateTransitGatewayPolicyTableResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
