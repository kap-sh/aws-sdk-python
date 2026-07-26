"""Generated from Smithy shape ``com.amazonaws.kafka#Firehose``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean
    import capo_kafka.types.__string


class Firehose(TypedDict, closed=True):
    delivery_stream: NotRequired["capo_kafka.types.__string.__string"]
    enabled: NotRequired["capo_kafka.types.__boolean.__boolean"]


# --- restJson1 ser/de ---
def serialize_json(value: Firehose) -> dict:
    out: dict = {}
    if "delivery_stream" in value:
        out["deliveryStream"] = value["delivery_stream"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> Firehose:
    out: Firehose = {}  # type: ignore[typeddict-item]
    if "deliveryStream" in data:
        out["delivery_stream"] = data["deliveryStream"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
