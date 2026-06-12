"""Generated from Smithy shape ``com.amazonaws.firehose#DescribeDeliveryStreamInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_name
    import aws_sdk_firehose.types.describe_delivery_stream_input_limit
    import aws_sdk_firehose.types.destination_id


class DescribeDeliveryStreamInput(TypedDict):
    delivery_stream_name: (
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Firehose stream.</p>"""
    limit: NotRequired[
        "aws_sdk_firehose.types.describe_delivery_stream_input_limit.DescribeDeliveryStreamInputLimit"
    ]
    """<p>The limit on the number of destinations to return. You can have one destination per Firehose stream.</p>"""
    exclusive_start_destination_id: NotRequired[
        "aws_sdk_firehose.types.destination_id.DestinationId"
    ]
    """<p>The ID of the destination to start returning the destination information. Firehose supports one destination per Firehose stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "exclusive_start_destination_id" in value:
        out["ExclusiveStartDestinationId"] = value["exclusive_start_destination_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryStreamInput:
    out: DescribeDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "DescribeDeliveryStreamInput.delivery_stream_name required"
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "ExclusiveStartDestinationId" in data:
        out["exclusive_start_destination_id"] = data["ExclusiveStartDestinationId"]
    return out
