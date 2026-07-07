"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#FirehoseLogDeliveryDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__boolean
    import aws_sdk_kafkaconnect.types.__string


class FirehoseLogDeliveryDescription(TypedDict, closed=True):
    delivery_stream: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.</p>"""
    enabled: "aws_sdk_kafkaconnect.types.__boolean.__boolean"
    """<p>Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseLogDeliveryDescription) -> dict:
    out: dict = {}
    if "delivery_stream" in value:
        out["deliveryStream"] = value["delivery_stream"]
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> FirehoseLogDeliveryDescription:
    out: FirehoseLogDeliveryDescription = {}  # type: ignore[typeddict-item]
    if "deliveryStream" in data:
        out["delivery_stream"] = data["deliveryStream"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
