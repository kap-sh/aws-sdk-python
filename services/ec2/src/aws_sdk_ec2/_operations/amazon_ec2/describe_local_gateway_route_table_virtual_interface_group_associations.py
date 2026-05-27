"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_request
    import aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_result


def describe_local_gateway_route_table_virtual_interface_group_associations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_request.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_result.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_local_gateway_route_table_virtual_interface_group_associations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_request.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_result.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
