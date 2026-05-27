"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTimeToLive``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_time_to_live_input
    import aws_sdk_dynamodb.types.describe_time_to_live_output


def describe_time_to_live(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_time_to_live_input.DescribeTimeToLiveInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_time_to_live_output.DescribeTimeToLiveOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_time_to_live(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_time_to_live_input.DescribeTimeToLiveInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_time_to_live_output.DescribeTimeToLiveOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
