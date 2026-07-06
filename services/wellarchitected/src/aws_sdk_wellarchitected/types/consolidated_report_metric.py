"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ConsolidatedReportMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_metrics
    import aws_sdk_wellarchitected.types.lenses_applied_count
    import aws_sdk_wellarchitected.types.metric_type
    import aws_sdk_wellarchitected.types.risk_counts
    import aws_sdk_wellarchitected.types.timestamp
    import aws_sdk_wellarchitected.types.workload_arn
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_name


class ConsolidatedReportMetric(TypedDict, closed=True):
    metric_type: NotRequired["aws_sdk_wellarchitected.types.metric_type.MetricType"]
    """<p>The metric type of a metric in the consolidated report. Currently only WORKLOAD metric types are supported.</p>"""
    risk_counts: NotRequired["aws_sdk_wellarchitected.types.risk_counts.RiskCounts"]
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    workload_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]
    workload_arn: NotRequired["aws_sdk_wellarchitected.types.workload_arn.WorkloadArn"]
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    lenses: NotRequired["aws_sdk_wellarchitected.types.lens_metrics.LensMetrics"]
    """<p>The metrics for the lenses in the workload.</p>"""
    lenses_applied_count: NotRequired[
        "aws_sdk_wellarchitected.types.lenses_applied_count.LensesAppliedCount"
    ]
    """<p>The total number of lenses applied to the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedReportMetric) -> dict:
    out: dict = {}
    if "metric_type" in value:
        import aws_sdk_wellarchitected.types.metric_type

        out["MetricType"] = aws_sdk_wellarchitected.types.metric_type.serialize_json(
            value["metric_type"]
        )
    if "risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["RiskCounts"] = aws_sdk_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "workload_arn" in value:
        out["WorkloadArn"] = value["workload_arn"]
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "lenses" in value:
        import aws_sdk_wellarchitected.types.lens_metrics

        out["Lenses"] = aws_sdk_wellarchitected.types.lens_metrics.serialize_json(
            value["lenses"]
        )
    if "lenses_applied_count" in value:
        out["LensesAppliedCount"] = value["lenses_applied_count"]
    return out


def deserialize_json(data: dict) -> ConsolidatedReportMetric:
    out: ConsolidatedReportMetric = {}  # type: ignore[typeddict-item]
    if "MetricType" in data:
        import aws_sdk_wellarchitected.types.metric_type

        out["metric_type"] = aws_sdk_wellarchitected.types.metric_type.deserialize_json(
            data["MetricType"]
        )
    if "RiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["risk_counts"] = aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "WorkloadArn" in data:
        out["workload_arn"] = data["WorkloadArn"]
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "Lenses" in data:
        import aws_sdk_wellarchitected.types.lens_metrics

        out["lenses"] = aws_sdk_wellarchitected.types.lens_metrics.deserialize_json(
            data["Lenses"]
        )
    if "LensesAppliedCount" in data:
        out["lenses_applied_count"] = data["LensesAppliedCount"]
    return out
