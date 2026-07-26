"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.current_metric_id
    import capo_connect.types.current_metric_name
    import capo_connect.types.unit


class CurrentMetric(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.current_metric_name.CurrentMetricName"]
    """<p>The name of the metric.</p>"""
    metric_id: NotRequired["capo_connect.types.current_metric_id.CurrentMetricId"]
    """<p>Out of the box current metrics or custom metrics can be referenced via this field. This field is a valid AWS Connect Arn or a UUID.</p>"""
    unit: NotRequired["capo_connect.types.unit.Unit"]
    """<note> <p>The Unit parameter is not supported for custom metrics.</p> </note> <p>The unit for the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_connect.types.current_metric_name

        out["Name"] = capo_connect.types.current_metric_name.serialize_json(
            value["name"]
        )
    if "metric_id" in value:
        out["MetricId"] = value["metric_id"]
    if "unit" in value:
        import capo_connect.types.unit

        out["Unit"] = capo_connect.types.unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> CurrentMetric:
    out: CurrentMetric = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_connect.types.current_metric_name

        out["name"] = capo_connect.types.current_metric_name.deserialize_json(
            data["Name"]
        )
    if "MetricId" in data:
        out["metric_id"] = data["MetricId"]
    if "Unit" in data:
        import capo_connect.types.unit

        out["unit"] = capo_connect.types.unit.deserialize_json(data["Unit"])
    return out
