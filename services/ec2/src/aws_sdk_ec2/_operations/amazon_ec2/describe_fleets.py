"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fleets_request
    import aws_sdk_ec2.types.describe_fleets_result


def describe_fleets(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_fleets_request.DescribeFleetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fleets_result.DescribeFleetsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_fleets(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_fleets_request.DescribeFleetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_fleets_result.DescribeFleetsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
