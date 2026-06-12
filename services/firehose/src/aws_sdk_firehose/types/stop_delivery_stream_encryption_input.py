"""Generated from Smithy shape ``com.amazonaws.firehose#StopDeliveryStreamEncryptionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_name


class StopDeliveryStreamEncryptionInput(TypedDict):
    delivery_stream_name: (
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Firehose stream for which you want to disable server-side encryption (SSE).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDeliveryStreamEncryptionInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDeliveryStreamEncryptionInput:
    out: StopDeliveryStreamEncryptionInput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "StopDeliveryStreamEncryptionInput.delivery_stream_name required"
        )
    return out
