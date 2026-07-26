"""Generated from Smithy shape ``com.amazonaws.pipes#FirehoseLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.firehose_arn


class FirehoseLogDestination(TypedDict, closed=True):
    delivery_stream_arn: NotRequired["capo_pipes.types.firehose_arn.FirehoseArn"]
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
