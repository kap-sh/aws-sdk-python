"""Generated from Smithy shape ``com.amazonaws.firehose#CreateDeliveryStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_arn


class CreateDeliveryStreamOutput(TypedDict, closed=True):
    delivery_stream_arn: NotRequired[
        "capo_firehose.types.delivery_stream_arn.DeliveryStreamARN"
    ]
    """<p>The ARN of the Firehose stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeliveryStreamOutput) -> dict:
    out: dict = {}
    if "delivery_stream_arn" in value:
        out["DeliveryStreamARN"] = value["delivery_stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeliveryStreamOutput:
    out: CreateDeliveryStreamOutput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamARN" in data:
        out["delivery_stream_arn"] = data["DeliveryStreamARN"]
    return out
