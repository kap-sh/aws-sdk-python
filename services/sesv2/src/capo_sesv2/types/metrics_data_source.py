"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricsDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.export_dimensions
    import capo_sesv2.types.export_metrics
    import capo_sesv2.types.metric_namespace
    import capo_sesv2.types.timestamp


class MetricsDataSource(TypedDict, closed=True):
    dimensions: "capo_sesv2.types.export_dimensions.ExportDimensions"
    """<p>An object that contains a mapping between a <code>MetricDimensionName</code> and <code>MetricDimensionValue</code> to filter metrics by. Must contain a least 1 dimension but no more than 3 unique ones.</p>"""
    namespace: "capo_sesv2.types.metric_namespace.MetricNamespace"
    """<p>The metrics namespace - e.g., <code>VDM</code>.</p>"""
    metrics: "capo_sesv2.types.export_metrics.ExportMetrics"
    """<p>A list of <code>ExportMetric</code> objects to export.</p>"""
    start_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the start date for the export interval as a timestamp.</p>"""
    end_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the end date for the export interval as a timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsDataSource) -> dict:
    out: dict = {}
    import capo_sesv2.types.export_dimensions

    out["Dimensions"] = capo_sesv2.types.export_dimensions.serialize_json(
        value["dimensions"]
    )
    import capo_sesv2.types.metric_namespace

    out["Namespace"] = capo_sesv2.types.metric_namespace.serialize_json(
        value["namespace"]
    )
    import capo_sesv2.types.export_metrics

    out["Metrics"] = capo_sesv2.types.export_metrics.serialize_json(value["metrics"])
    import capo_sesv2.types.timestamp

    out["StartDate"] = capo_sesv2.types.timestamp.serialize_json(value["start_date"])
    import capo_sesv2.types.timestamp

    out["EndDate"] = capo_sesv2.types.timestamp.serialize_json(value["end_date"])
    return out


def deserialize_json(data: dict) -> MetricsDataSource:
    out: MetricsDataSource = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_sesv2.types.export_dimensions

        out["dimensions"] = capo_sesv2.types.export_dimensions.deserialize_json(
            data["Dimensions"]
        )
    else:
        raise DeserializationError("MetricsDataSource.dimensions required")
    if "Namespace" in data:
        import capo_sesv2.types.metric_namespace

        out["namespace"] = capo_sesv2.types.metric_namespace.deserialize_json(
            data["Namespace"]
        )
    else:
        raise DeserializationError("MetricsDataSource.namespace required")
    if "Metrics" in data:
        import capo_sesv2.types.export_metrics

        out["metrics"] = capo_sesv2.types.export_metrics.deserialize_json(
            data["Metrics"]
        )
    else:
        raise DeserializationError("MetricsDataSource.metrics required")
    if "StartDate" in data:
        import capo_sesv2.types.timestamp

        out["start_date"] = capo_sesv2.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        raise DeserializationError("MetricsDataSource.start_date required")
    if "EndDate" in data:
        import capo_sesv2.types.timestamp

        out["end_date"] = capo_sesv2.types.timestamp.deserialize_json(data["EndDate"])
    else:
        raise DeserializationError("MetricsDataSource.end_date required")
    return out
