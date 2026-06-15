"""Generated from Smithy shape ``com.amazonaws.iotevents#FirehoseAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.delivery_stream_name
    import aws_sdk_iot_events.types.firehose_separator
    import aws_sdk_iot_events.types.payload


class FirehoseAction(TypedDict):
    delivery_stream_name: (
        "aws_sdk_iot_events.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Kinesis Data Firehose delivery stream where the data is written.</p>"""
    separator: NotRequired[
        "aws_sdk_iot_events.types.firehose_separator.FirehoseSeparator"
    ]
    r"""<p>A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).</p>"""
    payload: NotRequired["aws_sdk_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseAction) -> dict:
    out: dict = {}
    out["deliveryStreamName"] = value["delivery_stream_name"]
    if "separator" in value:
        out["separator"] = value["separator"]
    if "payload" in value:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> FirehoseAction:
    out: FirehoseAction = {}  # type: ignore[typeddict-item]
    if "deliveryStreamName" in data:
        out["delivery_stream_name"] = data["deliveryStreamName"]
    else:
        raise DeserializationError("FirehoseAction.delivery_stream_name required")
    if "separator" in data:
        out["separator"] = data["separator"]
    if "payload" in data:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.deserialize_json(
            data["payload"]
        )
    return out
