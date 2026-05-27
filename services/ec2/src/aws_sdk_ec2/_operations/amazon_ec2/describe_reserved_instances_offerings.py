"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesOfferings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_reserved_instances_offerings_request
    import aws_sdk_ec2.types.describe_reserved_instances_offerings_result


def describe_reserved_instances_offerings(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_reserved_instances_offerings_request.DescribeReservedInstancesOfferingsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_reserved_instances_offerings_result.DescribeReservedInstancesOfferingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_reserved_instances_offerings(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_reserved_instances_offerings_request.DescribeReservedInstancesOfferingsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_reserved_instances_offerings_result.DescribeReservedInstancesOfferingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
