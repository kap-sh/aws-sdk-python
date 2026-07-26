"""Generated from Smithy shape ``com.amazonaws.iot#MetricDatum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.metric_value
    import capo_iot.types.timestamp


class MetricDatum(TypedDict, closed=True):
    timestamp: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The time the metric value was reported.</p>"""
    value: NotRequired["capo_iot.types.metric_value.MetricValue"]
    """<p>The value reported for the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDatum) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_iot.types.timestamp

        out["timestamp"] = capo_iot.types.timestamp.serialize_json(value["timestamp"])
    if "value" in value:
        import capo_iot.types.metric_value

        out["value"] = capo_iot.types.metric_value.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> MetricDatum:
    out: MetricDatum = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import capo_iot.types.timestamp

        out["timestamp"] = capo_iot.types.timestamp.deserialize_json(data["timestamp"])
    if "value" in data:
        import capo_iot.types.metric_value

        out["value"] = capo_iot.types.metric_value.deserialize_json(data["value"])
    return out
