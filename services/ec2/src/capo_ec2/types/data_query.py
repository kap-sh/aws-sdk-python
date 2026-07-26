"""Generated from Smithy shape ``com.amazonaws.ec2#DataQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_type
    import capo_ec2.types.period_type
    import capo_ec2.types.statistic_type
    import capo_ec2.types.string


class DataQuery(TypedDict, closed=True):
    id: NotRequired["capo_ec2.types.string.String"]
    """<p>A user-defined ID associated with a data query that's returned in the <code>dataResponse</code> identifying the query. For example, if you set the Id to <code>MyQuery01</code>in the query, the <code>dataResponse</code> identifies the query as <code>MyQuery01</code>.</p>"""
    source: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the source for the data query. For example, <code>us-east-1</code>.</p>"""
    destination: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the target for the data query. For example, <code>eu-north-1</code>.</p>"""
    metric: NotRequired["capo_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the network performance request.</p>"""
    statistic: NotRequired["capo_ec2.types.statistic_type.StatisticType"]
    """<p>The metric data aggregation period, <code>p50</code>, between the specified <code>startDate</code> and <code>endDate</code>. For example, a metric of <code>five_minutes</code> is the median of all the data points gathered within those five minutes. <code>p50</code> is the only supported metric.</p>"""
    period: NotRequired["capo_ec2.types.period_type.PeriodType"]
    """<p>The aggregation period used for the data query.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DataQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "source" in value:
        pairs.append((f"{prefix}.Source", str(value["source"])))
    if "destination" in value:
        pairs.append((f"{prefix}.Destination", str(value["destination"])))
    if "metric" in value:
        import capo_ec2.types.metric_type

        capo_ec2.types.metric_type.serialize_ec2_query(
            value["metric"], pairs, f"{prefix}.Metric"
        )
    if "statistic" in value:
        import capo_ec2.types.statistic_type

        capo_ec2.types.statistic_type.serialize_ec2_query(
            value["statistic"], pairs, f"{prefix}.Statistic"
        )
    if "period" in value:
        import capo_ec2.types.period_type

        capo_ec2.types.period_type.serialize_ec2_query(
            value["period"], pairs, f"{prefix}.Period"
        )


def deserialize_ec2_query(el: Element) -> DataQuery:
    out: DataQuery = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_destination = el.find("Destination")
    if child_destination is not None:
        out["destination"] = str(child_destination.text or "")
    child_metric = el.find("Metric")
    if child_metric is not None:
        import capo_ec2.types.metric_type

        out["metric"] = capo_ec2.types.metric_type.deserialize_ec2_query(child_metric)
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import capo_ec2.types.statistic_type

        out["statistic"] = capo_ec2.types.statistic_type.deserialize_ec2_query(
            child_statistic
        )
    child_period = el.find("Period")
    if child_period is not None:
        import capo_ec2.types.period_type

        out["period"] = capo_ec2.types.period_type.deserialize_ec2_query(child_period)
    return out
