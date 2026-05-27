"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCustomerGateways``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_customer_gateways_request
    import aws_sdk_ec2.types.describe_customer_gateways_result


def describe_customer_gateways(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_customer_gateways_request.DescribeCustomerGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_customer_gateways_result.DescribeCustomerGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_customer_gateways(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_customer_gateways_request.DescribeCustomerGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_customer_gateways_result.DescribeCustomerGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
