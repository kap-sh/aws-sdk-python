"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisDataStreamDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.kinesis_data_stream_destination

KinesisDataStreamDestinations: TypeAlias = list[
    "aws_sdk_dynamodb.types.kinesis_data_stream_destination.KinesisDataStreamDestination"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KinesisDataStreamDestinations) -> list:
    import aws_sdk_dynamodb.types.kinesis_data_stream_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.kinesis_data_stream_destination.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> KinesisDataStreamDestinations:
    import aws_sdk_dynamodb.types.kinesis_data_stream_destination

    out: KinesisDataStreamDestinations = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.kinesis_data_stream_destination.deserialize_aws_json_1_0(
                item
            )
        )
    return out
