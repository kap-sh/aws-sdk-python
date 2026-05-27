"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestHistory``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_spot_fleet_request_history_request
    import aws_sdk_ec2.types.describe_spot_fleet_request_history_response


def describe_spot_fleet_request_history(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_spot_fleet_request_history_request.DescribeSpotFleetRequestHistoryRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_spot_fleet_request_history_response.DescribeSpotFleetRequestHistoryResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_spot_fleet_request_history(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_spot_fleet_request_history_request.DescribeSpotFleetRequestHistoryRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_spot_fleet_request_history_response.DescribeSpotFleetRequestHistoryResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
