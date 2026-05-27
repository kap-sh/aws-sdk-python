"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_request
    import aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_result


def create_local_gateway_route_table_virtual_interface_group_association(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_request.CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_result.CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_local_gateway_route_table_virtual_interface_group_association(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_request.CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_result.CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
