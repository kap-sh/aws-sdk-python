"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayMulticastDomainAssociations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_request
    import aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_result


def get_transit_gateway_multicast_domain_associations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_request.GetTransitGatewayMulticastDomainAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_result.GetTransitGatewayMulticastDomainAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_transit_gateway_multicast_domain_associations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_request.GetTransitGatewayMulticastDomainAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_result.GetTransitGatewayMulticastDomainAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
