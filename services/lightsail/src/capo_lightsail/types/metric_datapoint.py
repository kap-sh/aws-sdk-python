"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricDatapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.double
    import capo_lightsail.types.metric_unit
    import capo_lightsail.types.timestamp


class MetricDatapoint(TypedDict, closed=True):
    average: NotRequired["capo_lightsail.types.double.double"]
    """<p>The average.</p>"""
    maximum: NotRequired["capo_lightsail.types.double.double"]
    """<p>The maximum.</p>"""
    minimum: NotRequired["capo_lightsail.types.double.double"]
    """<p>The minimum.</p>"""
    sample_count: NotRequired["capo_lightsail.types.double.double"]
    """<p>The sample count.</p>"""
    sum: NotRequired["capo_lightsail.types.double.double"]
    """<p>The sum.</p>"""
    timestamp: NotRequired["capo_lightsail.types.timestamp.timestamp"]
    """<p>The timestamp (<code>1479816991.349</code>).</p>"""
    unit: NotRequired["capo_lightsail.types.metric_unit.MetricUnit"]
    """<p>The unit. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDatapoint) -> dict:
    out: dict = {}
    if "average" in value:
        out["average"] = value["average"]
    if "maximum" in value:
        out["maximum"] = value["maximum"]
    if "minimum" in value:
        out["minimum"] = value["minimum"]
    if "sample_count" in value:
        out["sampleCount"] = value["sample_count"]
    if "sum" in value:
        out["sum"] = value["sum"]
    if "timestamp" in value:
        import capo_lightsail.types.timestamp

        out["timestamp"] = capo_lightsail.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "unit" in value:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.serialize_aws_json_1_1(
            value["unit"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDatapoint:
    out: MetricDatapoint = {}  # type: ignore[typeddict-item]
    if "average" in data:
        out["average"] = data["average"]
    if "maximum" in data:
        out["maximum"] = data["maximum"]
    if "minimum" in data:
        out["minimum"] = data["minimum"]
    if "sampleCount" in data:
        out["sample_count"] = data["sampleCount"]
    if "sum" in data:
        out["sum"] = data["sum"]
    if "timestamp" in data:
        import capo_lightsail.types.timestamp

        out["timestamp"] = capo_lightsail.types.timestamp.deserialize_aws_json_1_1(
            data["timestamp"]
        )
    if "unit" in data:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    return out
