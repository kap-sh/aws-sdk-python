"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ConsolidatedReportMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.consolidated_report_metric

ConsolidatedReportMetrics: TypeAlias = list[
    "aws_sdk_wellarchitected.types.consolidated_report_metric.ConsolidatedReportMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedReportMetrics) -> list:
    import aws_sdk_wellarchitected.types.consolidated_report_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.consolidated_report_metric.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConsolidatedReportMetrics:
    import aws_sdk_wellarchitected.types.consolidated_report_metric

    out: ConsolidatedReportMetrics = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.consolidated_report_metric.deserialize_json(
                item
            )
        )
    return out
