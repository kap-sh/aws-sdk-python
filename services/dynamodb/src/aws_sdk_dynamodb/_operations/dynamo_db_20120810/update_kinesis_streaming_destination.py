"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateKinesisStreamingDestination``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.update_kinesis_streaming_destination_input
    import aws_sdk_dynamodb.types.update_kinesis_streaming_destination_output


def update_kinesis_streaming_destination(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.update_kinesis_streaming_destination_input.UpdateKinesisStreamingDestinationInput,
) -> tuple[
    aws_sdk_dynamodb.types.update_kinesis_streaming_destination_output.UpdateKinesisStreamingDestinationOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_kinesis_streaming_destination(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.update_kinesis_streaming_destination_input.UpdateKinesisStreamingDestinationInput,
) -> tuple[
    aws_sdk_dynamodb.types.update_kinesis_streaming_destination_output.UpdateKinesisStreamingDestinationOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
