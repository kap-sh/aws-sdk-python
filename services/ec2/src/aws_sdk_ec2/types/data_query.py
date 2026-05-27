"""Generated from Smithy shape ``com.amazonaws.ec2#DataQuery``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_type
    import aws_sdk_ec2.types.period_type
    import aws_sdk_ec2.types.statistic_type
    import aws_sdk_ec2.types.string


class DataQuery(TypedDict):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A user-defined ID associated with a data query that's returned in the <code>dataResponse</code> identifying the query. For example, if you set the Id to <code>MyQuery01</code>in the query, the <code>dataResponse</code> identifies the query as <code>MyQuery01</code>.</p>"""
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the source for the data query. For example, <code>us-east-1</code>.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the target for the data query. For example, <code>eu-north-1</code>.</p>"""
    metric: NotRequired["aws_sdk_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the network performance request.</p>"""
    statistic: NotRequired["aws_sdk_ec2.types.statistic_type.StatisticType"]
    """<p>The metric data aggregation period, <code>p50</code>, between the specified <code>startDate</code> and <code>endDate</code>. For example, a metric of <code>five_minutes</code> is the median of all the data points gathered within those five minutes. <code>p50</code> is the only supported metric.</p>"""
    period: NotRequired["aws_sdk_ec2.types.period_type.PeriodType"]
    """<p>The aggregation period used for the data query.</p>"""
