"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityManagerDataExports``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_capacity_manager_data_exports_request
    import aws_sdk_ec2.types.describe_capacity_manager_data_exports_result


def describe_capacity_manager_data_exports(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_capacity_manager_data_exports_request.DescribeCapacityManagerDataExportsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_capacity_manager_data_exports_result.DescribeCapacityManagerDataExportsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_capacity_manager_data_exports(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_capacity_manager_data_exports_request.DescribeCapacityManagerDataExportsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_capacity_manager_data_exports_result.DescribeCapacityManagerDataExportsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
