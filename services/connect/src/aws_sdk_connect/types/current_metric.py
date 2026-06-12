"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.current_metric_id
    import aws_sdk_connect.types.current_metric_name
    import aws_sdk_connect.types.unit


class CurrentMetric(TypedDict):
    name: NotRequired["aws_sdk_connect.types.current_metric_name.CurrentMetricName"]
    """<p>The name of the metric.</p>"""
    metric_id: NotRequired["aws_sdk_connect.types.current_metric_id.CurrentMetricId"]
    """<p>Out of the box current metrics or custom metrics can be referenced via this field. This field is a valid AWS Connect Arn or a UUID.</p>"""
    unit: NotRequired["aws_sdk_connect.types.unit.Unit"]
    """<note> <p>The Unit parameter is not supported for custom metrics.</p> </note> <p>The unit for the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_connect.types.current_metric_name

        out["Name"] = aws_sdk_connect.types.current_metric_name.serialize_json(
            value["name"]
        )
    if "metric_id" in value:
        out["MetricId"] = value["metric_id"]
    if "unit" in value:
        import aws_sdk_connect.types.unit

        out["Unit"] = aws_sdk_connect.types.unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> CurrentMetric:
    out: CurrentMetric = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_connect.types.current_metric_name

        out["name"] = aws_sdk_connect.types.current_metric_name.deserialize_json(
            data["Name"]
        )
    if "MetricId" in data:
        out["metric_id"] = data["MetricId"]
    if "Unit" in data:
        import aws_sdk_connect.types.unit

        out["unit"] = aws_sdk_connect.types.unit.deserialize_json(data["Unit"])
    return out
