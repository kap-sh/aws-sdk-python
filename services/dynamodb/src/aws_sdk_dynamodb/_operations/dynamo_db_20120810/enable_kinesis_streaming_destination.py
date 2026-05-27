"""Generated from Smithy shape ``com.amazonaws.dynamodb#EnableKinesisStreamingDestination``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.kinesis_streaming_destination_input
    import aws_sdk_dynamodb.types.kinesis_streaming_destination_output


def enable_kinesis_streaming_destination(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.kinesis_streaming_destination_input.KinesisStreamingDestinationInput,
) -> tuple[
    aws_sdk_dynamodb.types.kinesis_streaming_destination_output.KinesisStreamingDestinationOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_kinesis_streaming_destination(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.kinesis_streaming_destination_input.KinesisStreamingDestinationInput,
) -> tuple[
    aws_sdk_dynamodb.types.kinesis_streaming_destination_output.KinesisStreamingDestinationOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
