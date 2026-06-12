"""Generated from Smithy shape ``com.amazonaws.pipes#FirehoseLogDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.firehose_arn


class FirehoseLogDestination(TypedDict):
    delivery_stream_arn: NotRequired["aws_sdk_pipes.types.firehose_arn.FirehoseArn"]
    """<p>The Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseLogDestination) -> dict:
    out: dict = {}
    if "delivery_stream_arn" in value:
        out["DeliveryStreamArn"] = value["delivery_stream_arn"]
    return out


def deserialize_json(data: dict) -> FirehoseLogDestination:
    out: FirehoseLogDestination = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamArn" in data:
        out["delivery_stream_arn"] = data["DeliveryStreamArn"]
    return out
