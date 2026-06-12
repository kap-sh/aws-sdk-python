"""Generated from Smithy shape ``com.amazonaws.iot#MetricDatum``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.metric_value
    import aws_sdk_iot.types.timestamp


class MetricDatum(TypedDict):
    timestamp: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The time the metric value was reported.</p>"""
    value: NotRequired["aws_sdk_iot.types.metric_value.MetricValue"]
    """<p>The value reported for the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDatum) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_iot.types.timestamp

        out["timestamp"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "value" in value:
        import aws_sdk_iot.types.metric_value

        out["value"] = aws_sdk_iot.types.metric_value.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> MetricDatum:
    out: MetricDatum = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import aws_sdk_iot.types.timestamp

        out["timestamp"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["timestamp"]
        )
    if "value" in data:
        import aws_sdk_iot.types.metric_value

        out["value"] = aws_sdk_iot.types.metric_value.deserialize_json(data["value"])
    return out
