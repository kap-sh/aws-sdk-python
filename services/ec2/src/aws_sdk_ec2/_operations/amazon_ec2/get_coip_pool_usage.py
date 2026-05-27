"""Generated from Smithy shape ``com.amazonaws.ec2#GetCoipPoolUsage``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_coip_pool_usage_request
    import aws_sdk_ec2.types.get_coip_pool_usage_result


def get_coip_pool_usage(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_coip_pool_usage_request.GetCoipPoolUsageRequest,
) -> tuple[
    aws_sdk_ec2.types.get_coip_pool_usage_result.GetCoipPoolUsageResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_coip_pool_usage(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_coip_pool_usage_request.GetCoipPoolUsageRequest,
) -> tuple[
    aws_sdk_ec2.types.get_coip_pool_usage_result.GetCoipPoolUsageResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
