"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fleet_instances_request
    import aws_sdk_ec2.types.describe_fleet_instances_result


def describe_fleet_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_fleet_instances_request.DescribeFleetInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fleet_instances_result.DescribeFleetInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_fleet_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_fleet_instances_request.DescribeFleetInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fleet_instances_result.DescribeFleetInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
