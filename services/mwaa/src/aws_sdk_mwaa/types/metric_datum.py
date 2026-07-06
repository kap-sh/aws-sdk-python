"""Generated from Smithy shape ``com.amazonaws.mwaa#MetricDatum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mwaa.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mwaa.types.dimensions
    import aws_sdk_mwaa.types.statistic_set
    import aws_sdk_mwaa.types.unit


class MetricDatum(TypedDict, closed=True):
    metric_name: "str"
    """<p> <b>Internal only</b>. The name of the metric.</p>"""
    timestamp: "datetime.datetime"
    """<p> <b>Internal only</b>. The time the metric data was received, expressed as an ISO 8601 datetime string.</p>"""
    dimensions: NotRequired["aws_sdk_mwaa.types.dimensions.Dimensions"]
    """<p> <b>Internal only</b>. The dimensions associated with the metric.</p>"""
    value: NotRequired["float"]
    """<p> <b>Internal only</b>. The value for the metric.</p>"""
    unit: NotRequired["aws_sdk_mwaa.types.unit.Unit"]
    """<p> <b>Internal only</b>. The unit used to store the metric.</p>"""
    statistic_values: NotRequired["aws_sdk_mwaa.types.statistic_set.StatisticSet"]
    """<p> <b>Internal only</b>. The statistical values for the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDatum) -> dict:
    out: dict = {}
    out["MetricName"] = value["metric_name"]
    import aws_sdk_mwaa.types._prelude.timestamp

    out["Timestamp"] = aws_sdk_mwaa.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "dimensions" in value:
        import aws_sdk_mwaa.types.dimensions

        out["Dimensions"] = aws_sdk_mwaa.types.dimensions.serialize_json(
            value["dimensions"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    if "statistic_values" in value:
        import aws_sdk_mwaa.types.statistic_set

        out["StatisticValues"] = aws_sdk_mwaa.types.statistic_set.serialize_json(
            value["statistic_values"]
        )
    return out


def deserialize_json(data: dict) -> MetricDatum:
    out: MetricDatum = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("MetricDatum.metric_name required")
    if "Timestamp" in data:
        import aws_sdk_mwaa.types._prelude.timestamp

        out["timestamp"] = aws_sdk_mwaa.types._prelude.timestamp.deserialize_json(
            data["Timestamp"]
        )
    else:
        raise DeserializationError("MetricDatum.timestamp required")
    if "Dimensions" in data:
        import aws_sdk_mwaa.types.dimensions

        out["dimensions"] = aws_sdk_mwaa.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "StatisticValues" in data:
        import aws_sdk_mwaa.types.statistic_set

        out["statistic_values"] = aws_sdk_mwaa.types.statistic_set.deserialize_json(
            data["StatisticValues"]
        )
    return out
