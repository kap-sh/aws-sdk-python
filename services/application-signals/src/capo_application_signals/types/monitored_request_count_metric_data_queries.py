"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MonitoredRequestCountMetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_application_signals.types.metric_data_queries


class _MonitoredRequestCountMetricDataQueries_GoodCountMetric(TypedDict, closed=True):
    GoodCountMetric: (
        "capo_application_signals.types.metric_data_queries.MetricDataQueries"
    )


class _MonitoredRequestCountMetricDataQueries_BadCountMetric(TypedDict, closed=True):
    BadCountMetric: (
        "capo_application_signals.types.metric_data_queries.MetricDataQueries"
    )


MonitoredRequestCountMetricDataQueries: TypeAlias = (
    _MonitoredRequestCountMetricDataQueries_GoodCountMetric
    | _MonitoredRequestCountMetricDataQueries_BadCountMetric
)


# --- restJson1 ser/de ---
def serialize_json(value: MonitoredRequestCountMetricDataQueries) -> dict:
    if "GoodCountMetric" in value:
        import capo_application_signals.types.metric_data_queries

        return {
            "GoodCountMetric": capo_application_signals.types.metric_data_queries.serialize_json(
                value["GoodCountMetric"]
            )
        }
    elif "BadCountMetric" in value:
        import capo_application_signals.types.metric_data_queries

        return {
            "BadCountMetric": capo_application_signals.types.metric_data_queries.serialize_json(
                value["BadCountMetric"]
            )
        }
    else:
        raise SerializationError(
            "MonitoredRequestCountMetricDataQueries: no variant present"
        )


def deserialize_json(data: dict) -> MonitoredRequestCountMetricDataQueries:
    if "GoodCountMetric" in data:
        import capo_application_signals.types.metric_data_queries

        return {
            "GoodCountMetric": capo_application_signals.types.metric_data_queries.deserialize_json(
                data["GoodCountMetric"]
            )
        }
    elif "BadCountMetric" in data:
        import capo_application_signals.types.metric_data_queries

        return {
            "BadCountMetric": capo_application_signals.types.metric_data_queries.deserialize_json(
                data["BadCountMetric"]
            )
        }
    else:
        raise DeserializationError(
            "MonitoredRequestCountMetricDataQueries: no recognized variant key"
        )
