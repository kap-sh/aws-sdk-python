"""Generated from Smithy shape ``com.amazonaws.notifications#AggregationKey``."""

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError


class AggregationKey(TypedDict, closed=True):
    name: "str"
    """<p>Indicates the type of aggregation key.</p>"""
    value: "str"
    """<p>Indicates the value associated with the aggregation key name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationKey) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AggregationKey:
    out: AggregationKey = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AggregationKey.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("AggregationKey.value required")
    return out
