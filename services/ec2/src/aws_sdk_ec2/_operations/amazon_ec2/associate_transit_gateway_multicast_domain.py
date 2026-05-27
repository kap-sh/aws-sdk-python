"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTransitGatewayMulticastDomain``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_request
    import aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_result


def associate_transit_gateway_multicast_domain(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_request.AssociateTransitGatewayMulticastDomainRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_result.AssociateTransitGatewayMulticastDomainResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_transit_gateway_multicast_domain(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_request.AssociateTransitGatewayMulticastDomainRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_result.AssociateTransitGatewayMulticastDomainResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
