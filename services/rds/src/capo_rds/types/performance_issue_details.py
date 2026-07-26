"""Generated from Smithy shape ``com.amazonaws.rds#PerformanceIssueDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.metric_list
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class PerformanceIssueDetails(TypedDict, closed=True):
    start_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the performance issue started.</p>"""
    end_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the performance issue stopped.</p>"""
    metrics: NotRequired["capo_rds.types.metric_list.MetricList"]
    """<p>The metrics that are relevant to the performance issue.</p>"""
    analysis: NotRequired["capo_rds.types.string.String"]
    """<p>The analysis of the performance issue. The information might contain markdown.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PerformanceIssueDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "start_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "metrics" in value:
        import capo_rds.types.metric_list

        capo_rds.types.metric_list.serialize_query(
            value["metrics"], pairs, f"{prefix}.Metrics"
        )
    if "analysis" in value:
        pairs.append((f"{prefix}.Analysis", str(value["analysis"])))


def deserialize_query(el: Element) -> PerformanceIssueDetails:
    out: PerformanceIssueDetails = {}  # type: ignore[typeddict-item]
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_rds.types.t_stamp

        out["start_time"] = capo_rds.types.t_stamp.deserialize_query(child_start_time)
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_rds.types.t_stamp

        out["end_time"] = capo_rds.types.t_stamp.deserialize_query(child_end_time)
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_rds.types.metric_list

        out["metrics"] = capo_rds.types.metric_list.deserialize_query(child_metrics)
    child_analysis = el.find("Analysis")
    if child_analysis is not None:
        out["analysis"] = str(child_analysis.text or "")
    return out
