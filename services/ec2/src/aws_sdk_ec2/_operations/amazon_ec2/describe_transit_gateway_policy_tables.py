"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayPolicyTables``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_transit_gateway_policy_tables_request
    import aws_sdk_ec2.types.describe_transit_gateway_policy_tables_result


def describe_transit_gateway_policy_tables(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_transit_gateway_policy_tables_request.DescribeTransitGatewayPolicyTablesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_transit_gateway_policy_tables_result.DescribeTransitGatewayPolicyTablesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_transit_gateway_policy_tables(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_transit_gateway_policy_tables_request.DescribeTransitGatewayPolicyTablesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_transit_gateway_policy_tables_result.DescribeTransitGatewayPolicyTablesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
