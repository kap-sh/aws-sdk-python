"""Generated from Smithy shape ``com.amazonaws.rum#MetricDestinationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.metric_destination_summary

MetricDestinationSummaryList: TypeAlias = list[
    "capo_rum.types.metric_destination_summary.MetricDestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDestinationSummaryList) -> list:
    import capo_rum.types.metric_destination_summary

    out: list = []
    for item in value:
        out.append(capo_rum.types.metric_destination_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDestinationSummaryList:
    import capo_rum.types.metric_destination_summary

    out: MetricDestinationSummaryList = []
    for item in data:
        out.append(capo_rum.types.metric_destination_summary.deserialize_json(item))
    return out
