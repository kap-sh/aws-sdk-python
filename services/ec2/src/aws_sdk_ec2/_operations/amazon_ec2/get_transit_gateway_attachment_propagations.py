"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayAttachmentPropagations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_request
    import aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_result


def get_transit_gateway_attachment_propagations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_request.GetTransitGatewayAttachmentPropagationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_result.GetTransitGatewayAttachmentPropagationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_transit_gateway_attachment_propagations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_request.GetTransitGatewayAttachmentPropagationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_result.GetTransitGatewayAttachmentPropagationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
