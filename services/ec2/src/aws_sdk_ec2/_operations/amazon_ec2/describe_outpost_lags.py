"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeOutpostLags``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_outpost_lags_request
    import aws_sdk_ec2.types.describe_outpost_lags_result


def describe_outpost_lags(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_outpost_lags_request.DescribeOutpostLagsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_outpost_lags_result.DescribeOutpostLagsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_outpost_lags(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_outpost_lags_request.DescribeOutpostLagsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_outpost_lags_result.DescribeOutpostLagsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
