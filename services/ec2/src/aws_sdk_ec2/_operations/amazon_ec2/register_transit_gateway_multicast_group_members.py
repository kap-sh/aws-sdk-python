"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupMembers``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_request
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_result


def register_transit_gateway_multicast_group_members(
    options: OperationOptions,
    input: aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_request.RegisterTransitGatewayMulticastGroupMembersRequest,
) -> tuple[
    aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_result.RegisterTransitGatewayMulticastGroupMembersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_register_transit_gateway_multicast_group_members(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_request.RegisterTransitGatewayMulticastGroupMembersRequest,
) -> tuple[
    aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_result.RegisterTransitGatewayMulticastGroupMembersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
