"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeEgressOnlyInternetGateways``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_egress_only_internet_gateways_request
    import aws_sdk_ec2.types.describe_egress_only_internet_gateways_result


def describe_egress_only_internet_gateways(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_egress_only_internet_gateways_request.DescribeEgressOnlyInternetGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_egress_only_internet_gateways_result.DescribeEgressOnlyInternetGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_egress_only_internet_gateways(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_egress_only_internet_gateways_request.DescribeEgressOnlyInternetGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_egress_only_internet_gateways_result.DescribeEgressOnlyInternetGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
