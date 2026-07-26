"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.metric_data_query

MetricDataQueries: TypeAlias = list[
    "capo_application_signals.types.metric_data_query.MetricDataQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataQueries) -> list:
    import capo_application_signals.types.metric_data_query

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.metric_data_query.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetricDataQueries:
    import capo_application_signals.types.metric_data_query

    out: MetricDataQueries = []
    for item in data:
        out.append(
            capo_application_signals.types.metric_data_query.deserialize_json(item)
        )
    return out
