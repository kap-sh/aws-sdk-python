"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricDatapoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.double
    import aws_sdk_lightsail.types.metric_unit
    import aws_sdk_lightsail.types.timestamp


class MetricDatapoint(TypedDict):
    average: NotRequired["aws_sdk_lightsail.types.double.double"]
    """<p>The average.</p>"""
    maximum: NotRequired["aws_sdk_lightsail.types.double.double"]
    """<p>The maximum.</p>"""
    minimum: NotRequired["aws_sdk_lightsail.types.double.double"]
    """<p>The minimum.</p>"""
    sample_count: NotRequired["aws_sdk_lightsail.types.double.double"]
    """<p>The sample count.</p>"""
    sum: NotRequired["aws_sdk_lightsail.types.double.double"]
    """<p>The sum.</p>"""
    timestamp: NotRequired["aws_sdk_lightsail.types.timestamp.timestamp"]
    """<p>The timestamp (<code>1479816991.349</code>).</p>"""
    unit: NotRequired["aws_sdk_lightsail.types.metric_unit.MetricUnit"]
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
        import aws_sdk_lightsail.types.timestamp

        out["timestamp"] = aws_sdk_lightsail.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "unit" in value:
        import aws_sdk_lightsail.types.metric_unit

        out["unit"] = aws_sdk_lightsail.types.metric_unit.serialize_aws_json_1_1(
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
        import aws_sdk_lightsail.types.timestamp

        out["timestamp"] = aws_sdk_lightsail.types.timestamp.deserialize_aws_json_1_1(
            data["timestamp"]
        )
    if "unit" in data:
        import aws_sdk_lightsail.types.metric_unit

        out["unit"] = aws_sdk_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    return out
