"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeKinesisStreamingDestination``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_kinesis_streaming_destination_input
    import aws_sdk_dynamodb.types.describe_kinesis_streaming_destination_output


def describe_kinesis_streaming_destination(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_kinesis_streaming_destination_input.DescribeKinesisStreamingDestinationInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_kinesis_streaming_destination_output.DescribeKinesisStreamingDestinationOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_kinesis_streaming_destination(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_kinesis_streaming_destination_input.DescribeKinesisStreamingDestinationInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_kinesis_streaming_destination_output.DescribeKinesisStreamingDestinationOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
