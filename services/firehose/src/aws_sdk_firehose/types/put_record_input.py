"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_name
    import aws_sdk_firehose.types.record


class PutRecordInput(TypedDict):
    delivery_stream_name: (
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Firehose stream.</p>"""
    record: "aws_sdk_firehose.types.record.Record"
    """<p>The record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    import aws_sdk_firehose.types.record

    out["Record"] = aws_sdk_firehose.types.record.serialize_aws_json_1_1(
        value["record"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordInput:
    out: PutRecordInput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError("PutRecordInput.delivery_stream_name required")
    if "Record" in data:
        import aws_sdk_firehose.types.record

        out["record"] = aws_sdk_firehose.types.record.deserialize_aws_json_1_1(
            data["Record"]
        )
    else:
        raise DeserializationError("PutRecordInput.record required")
    return out
