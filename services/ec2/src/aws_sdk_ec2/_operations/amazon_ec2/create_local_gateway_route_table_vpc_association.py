"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableVpcAssociation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_request
    import aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_result


def create_local_gateway_route_table_vpc_association(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_request.CreateLocalGatewayRouteTableVpcAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_result.CreateLocalGatewayRouteTableVpcAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_local_gateway_route_table_vpc_association(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_request.CreateLocalGatewayRouteTableVpcAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_result.CreateLocalGatewayRouteTableVpcAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
