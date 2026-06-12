"""Generated from Smithy shape ``com.amazonaws.pipes#FirehoseLogDestinationParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.firehose_arn


class FirehoseLogDestinationParameters(TypedDict):
    delivery_stream_arn: "aws_sdk_pipes.types.firehose_arn.FirehoseArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseLogDestinationParameters) -> dict:
    out: dict = {}
    out["DeliveryStreamArn"] = value["delivery_stream_arn"]
    return out


def deserialize_json(data: dict) -> FirehoseLogDestinationParameters:
    out: FirehoseLogDestinationParameters = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamArn" in data:
        out["delivery_stream_arn"] = data["DeliveryStreamArn"]
    else:
        raise DeserializationError(
            "FirehoseLogDestinationParameters.delivery_stream_arn required"
        )
    return out
