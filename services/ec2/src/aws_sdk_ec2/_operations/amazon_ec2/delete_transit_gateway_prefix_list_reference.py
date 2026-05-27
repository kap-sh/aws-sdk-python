"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayPrefixListReference``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_request
    import aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_result


def delete_transit_gateway_prefix_list_reference(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_request.DeleteTransitGatewayPrefixListReferenceRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_result.DeleteTransitGatewayPrefixListReferenceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_transit_gateway_prefix_list_reference(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_request.DeleteTransitGatewayPrefixListReferenceRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_result.DeleteTransitGatewayPrefixListReferenceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
