"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ConsolidatedReportMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.consolidated_report_metric

ConsolidatedReportMetrics: TypeAlias = list[
    "capo_wellarchitected.types.consolidated_report_metric.ConsolidatedReportMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedReportMetrics) -> list:
    import capo_wellarchitected.types.consolidated_report_metric

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.consolidated_report_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConsolidatedReportMetrics:
    import capo_wellarchitected.types.consolidated_report_metric

    out: ConsolidatedReportMetrics = []
    for item in data:
        out.append(
            capo_wellarchitected.types.consolidated_report_metric.deserialize_json(item)
        )
    return out
