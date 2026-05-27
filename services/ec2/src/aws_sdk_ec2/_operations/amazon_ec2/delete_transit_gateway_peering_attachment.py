"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayPeeringAttachment``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_request
    import aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_result


def delete_transit_gateway_peering_attachment(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_request.DeleteTransitGatewayPeeringAttachmentRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_result.DeleteTransitGatewayPeeringAttachmentResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_transit_gateway_peering_attachment(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_request.DeleteTransitGatewayPeeringAttachmentRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_result.DeleteTransitGatewayPeeringAttachmentResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
