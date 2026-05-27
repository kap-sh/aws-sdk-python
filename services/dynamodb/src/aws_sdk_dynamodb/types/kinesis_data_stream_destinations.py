"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisDataStreamDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.kinesis_data_stream_destination

KinesisDataStreamDestinations: TypeAlias = list[
    "aws_sdk_dynamodb.types.kinesis_data_stream_destination.KinesisDataStreamDestination"
]
