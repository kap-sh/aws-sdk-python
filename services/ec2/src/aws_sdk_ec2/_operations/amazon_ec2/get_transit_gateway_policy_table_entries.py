"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPolicyTableEntries``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_request
    import aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_result


def get_transit_gateway_policy_table_entries(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_request.GetTransitGatewayPolicyTableEntriesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_result.GetTransitGatewayPolicyTableEntriesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_transit_gateway_policy_table_entries(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_request.GetTransitGatewayPolicyTableEntriesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_result.GetTransitGatewayPolicyTableEntriesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
