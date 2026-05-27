"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_spot_fleet_instances_request
    import aws_sdk_ec2.types.describe_spot_fleet_instances_response


def describe_spot_fleet_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_spot_fleet_instances_request.DescribeSpotFleetInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_spot_fleet_instances_response.DescribeSpotFleetInstancesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_spot_fleet_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_spot_fleet_instances_request.DescribeSpotFleetInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_spot_fleet_instances_response.DescribeSpotFleetInstancesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
