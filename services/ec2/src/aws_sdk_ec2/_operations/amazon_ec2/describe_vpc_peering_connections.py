"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcPeeringConnections``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_vpc_peering_connections_request
    import aws_sdk_ec2.types.describe_vpc_peering_connections_result


def describe_vpc_peering_connections(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_vpc_peering_connections_request.DescribeVpcPeeringConnectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpc_peering_connections_result.DescribeVpcPeeringConnectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_vpc_peering_connections(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_vpc_peering_connections_request.DescribeVpcPeeringConnectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpc_peering_connections_result.DescribeVpcPeeringConnectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
