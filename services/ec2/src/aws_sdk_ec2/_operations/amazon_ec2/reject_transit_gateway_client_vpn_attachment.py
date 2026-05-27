"""Generated from Smithy shape ``com.amazonaws.ec2#RejectTransitGatewayClientVpnAttachment``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_request
    import aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_result


def reject_transit_gateway_client_vpn_attachment(
    options: OperationOptions,
    input: aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_request.RejectTransitGatewayClientVpnAttachmentRequest,
) -> tuple[
    aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_result.RejectTransitGatewayClientVpnAttachmentResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_reject_transit_gateway_client_vpn_attachment(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_request.RejectTransitGatewayClientVpnAttachmentRequest,
) -> tuple[
    aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_result.RejectTransitGatewayClientVpnAttachmentResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
