"""Generated from Smithy shape ``com.amazonaws.ec2#RejectTransitGatewayMulticastDomainAssociations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_request
    import aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_result


def reject_transit_gateway_multicast_domain_associations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_request.RejectTransitGatewayMulticastDomainAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_result.RejectTransitGatewayMulticastDomainAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_reject_transit_gateway_multicast_domain_associations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_request.RejectTransitGatewayMulticastDomainAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_result.RejectTransitGatewayMulticastDomainAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
