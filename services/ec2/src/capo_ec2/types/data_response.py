"""Generated from Smithy shape ``com.amazonaws.ec2#DataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_points
    import capo_ec2.types.metric_type
    import capo_ec2.types.period_type
    import capo_ec2.types.statistic_type
    import capo_ec2.types.string


class DataResponse(TypedDict, closed=True):
    id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID passed in the <code>DataQuery</code>.</p>"""
    source: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the source for the data query. For example, <code>us-east-1</code>.</p>"""
    destination: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the destination for the data query. For example, <code>eu-west-1</code>.</p>"""
    metric: NotRequired["capo_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the network performance request.</p>"""
    statistic: NotRequired["capo_ec2.types.statistic_type.StatisticType"]
    """<p>The statistic used for the network performance request.</p>"""
    period: NotRequired["capo_ec2.types.period_type.PeriodType"]
    """<p>The period used for the network performance request.</p>"""
    metric_points: NotRequired["capo_ec2.types.metric_points.MetricPoints"]
    """<p>A list of <code>MetricPoint</code> objects.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DataResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "destination" in value:
        pairs.append((f"{key_prefix}Destination", str(value["destination"])))
    if "metric" in value:
        import capo_ec2.types.metric_type

        capo_ec2.types.metric_type.serialize_ec2_query(
            value["metric"], pairs, f"{key_prefix}Metric"
        )
    if "statistic" in value:
        import capo_ec2.types.statistic_type

        capo_ec2.types.statistic_type.serialize_ec2_query(
            value["statistic"], pairs, f"{key_prefix}Statistic"
        )
    if "period" in value:
        import capo_ec2.types.period_type

        capo_ec2.types.period_type.serialize_ec2_query(
            value["period"], pairs, f"{key_prefix}Period"
        )
    if "metric_points" in value:
        import capo_ec2.types.metric_points

        capo_ec2.types.metric_points.serialize_ec2_query(
            value["metric_points"], pairs, f"{key_prefix}MetricPointSet"
        )


def deserialize_ec2_query(el: Element) -> DataResponse:
    out: DataResponse = {}  # type: ignore[typeddict-item]
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
    if el.find("MetricPointSet") is not None:
        import capo_ec2.types.metric_points

        out["metric_points"] = capo_ec2.types.metric_points.deserialize_ec2_query(
            el, "MetricPointSet"
        )
    return out
