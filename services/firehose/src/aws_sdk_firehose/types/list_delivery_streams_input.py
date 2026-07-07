"""Generated from Smithy shape ``com.amazonaws.firehose#ListDeliveryStreamsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_name
    import aws_sdk_firehose.types.delivery_stream_type
    import aws_sdk_firehose.types.list_delivery_streams_input_limit


class ListDeliveryStreamsInput(TypedDict, closed=True):
    limit: NotRequired[
        "aws_sdk_firehose.types.list_delivery_streams_input_limit.ListDeliveryStreamsInputLimit"
    ]
    """<p>The maximum number of Firehose streams to list. The default value is 10.</p>"""
    delivery_stream_type: NotRequired[
        "aws_sdk_firehose.types.delivery_stream_type.DeliveryStreamType"
    ]
    """<p>The Firehose stream type. This can be one of the following values:</p> <ul> <li> <p> <code>DirectPut</code>: Provider applications access the Firehose stream directly.</p> </li> <li> <p> <code>KinesisStreamAsSource</code>: The Firehose stream uses a Kinesis data stream as a source.</p> </li> </ul> <p>This parameter is optional. If this parameter is omitted, Firehose streams of all types are returned.</p>"""
    exclusive_start_delivery_stream_name: NotRequired[
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    ]
    """<p>The list of Firehose streams returned by this call to <code>ListDeliveryStreams</code> will start with the Firehose stream whose name comes alphabetically immediately after the name you specify in <code>ExclusiveStartDeliveryStreamName</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeliveryStreamsInput) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "delivery_stream_type" in value:
        import aws_sdk_firehose.types.delivery_stream_type

        out["DeliveryStreamType"] = (
            aws_sdk_firehose.types.delivery_stream_type.serialize_aws_json_1_1(
                value["delivery_stream_type"]
            )
        )
    if "exclusive_start_delivery_stream_name" in value:
        out["ExclusiveStartDeliveryStreamName"] = value[
            "exclusive_start_delivery_stream_name"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeliveryStreamsInput:
    out: ListDeliveryStreamsInput = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "DeliveryStreamType" in data:
        import aws_sdk_firehose.types.delivery_stream_type

        out["delivery_stream_type"] = (
            aws_sdk_firehose.types.delivery_stream_type.deserialize_aws_json_1_1(
                data["DeliveryStreamType"]
            )
        )
    if "ExclusiveStartDeliveryStreamName" in data:
        out["exclusive_start_delivery_stream_name"] = data[
            "ExclusiveStartDeliveryStreamName"
        ]
    return out
