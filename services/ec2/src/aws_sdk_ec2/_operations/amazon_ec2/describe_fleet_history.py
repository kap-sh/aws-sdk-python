"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetHistory``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fleet_history_request
    import aws_sdk_ec2.types.describe_fleet_history_result


def describe_fleet_history(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_fleet_history_request.DescribeFleetHistoryRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fleet_history_result.DescribeFleetHistoryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_fleet_history(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_fleet_history_request.DescribeFleetHistoryRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fleet_history_result.DescribeFleetHistoryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
