"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTables``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_local_gateway_route_tables_request
    import aws_sdk_ec2.types.describe_local_gateway_route_tables_result


def describe_local_gateway_route_tables(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_local_gateway_route_tables_request.DescribeLocalGatewayRouteTablesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_local_gateway_route_tables_result.DescribeLocalGatewayRouteTablesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_local_gateway_route_tables(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_local_gateway_route_tables_request.DescribeLocalGatewayRouteTablesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_local_gateway_route_tables_result.DescribeLocalGatewayRouteTablesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
