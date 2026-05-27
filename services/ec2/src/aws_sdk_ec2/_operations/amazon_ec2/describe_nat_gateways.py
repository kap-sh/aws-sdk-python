"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNatGateways``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_nat_gateways_request
    import aws_sdk_ec2.types.describe_nat_gateways_result


def describe_nat_gateways(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_nat_gateways_request.DescribeNatGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_nat_gateways_result.DescribeNatGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_nat_gateways(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_nat_gateways_request.DescribeNatGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_nat_gateways_result.DescribeNatGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
