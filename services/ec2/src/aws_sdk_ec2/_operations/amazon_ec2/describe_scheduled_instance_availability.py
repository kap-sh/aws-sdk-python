"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstanceAvailability``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_scheduled_instance_availability_request
    import aws_sdk_ec2.types.describe_scheduled_instance_availability_result


def describe_scheduled_instance_availability(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_scheduled_instance_availability_request.DescribeScheduledInstanceAvailabilityRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_scheduled_instance_availability_result.DescribeScheduledInstanceAvailabilityResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_scheduled_instance_availability(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_scheduled_instance_availability_request.DescribeScheduledInstanceAvailabilityRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_scheduled_instance_availability_result.DescribeScheduledInstanceAvailabilityResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
