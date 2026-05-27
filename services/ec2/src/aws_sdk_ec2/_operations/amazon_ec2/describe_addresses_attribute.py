"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressesAttribute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_addresses_attribute_request
    import aws_sdk_ec2.types.describe_addresses_attribute_result


def describe_addresses_attribute(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_addresses_attribute_request.DescribeAddressesAttributeRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_addresses_attribute_result.DescribeAddressesAttributeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_addresses_attribute(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_addresses_attribute_request.DescribeAddressesAttributeRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_addresses_attribute_result.DescribeAddressesAttributeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
