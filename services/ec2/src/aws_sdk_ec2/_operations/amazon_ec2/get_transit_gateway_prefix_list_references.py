"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPrefixListReferences``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_request
    import aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_result


def get_transit_gateway_prefix_list_references(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_request.GetTransitGatewayPrefixListReferencesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_result.GetTransitGatewayPrefixListReferencesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_transit_gateway_prefix_list_references(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_request.GetTransitGatewayPrefixListReferencesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_result.GetTransitGatewayPrefixListReferencesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
