"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVpcAssociations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_request
    import aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_result


def describe_local_gateway_route_table_vpc_associations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_request.DescribeLocalGatewayRouteTableVpcAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_result.DescribeLocalGatewayRouteTableVpcAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_local_gateway_route_table_vpc_associations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_request.DescribeLocalGatewayRouteTableVpcAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_result.DescribeLocalGatewayRouteTableVpcAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
