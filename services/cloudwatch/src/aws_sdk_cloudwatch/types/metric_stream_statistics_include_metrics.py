"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamStatisticsIncludeMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_metric

MetricStreamStatisticsIncludeMetrics: TypeAlias = list[
    "aws_sdk_cloudwatch.types.metric_stream_statistics_metric.MetricStreamStatisticsMetric"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamStatisticsIncludeMetrics,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_metric

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.metric_stream_statistics_metric.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricStreamStatisticsIncludeMetrics:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_metric

    out: MetricStreamStatisticsIncludeMetrics = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudwatch.types.metric_stream_statistics_metric.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: MetricStreamStatisticsIncludeMetrics,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_metric

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.metric_stream_statistics_metric.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> MetricStreamStatisticsIncludeMetrics:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_metric

    out: MetricStreamStatisticsIncludeMetrics = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudwatch.types.metric_stream_statistics_metric.deserialize_query(
                child
            )
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamStatisticsIncludeMetrics) -> list:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.metric_stream_statistics_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricStreamStatisticsIncludeMetrics:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_metric

    out: MetricStreamStatisticsIncludeMetrics = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.metric_stream_statistics_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
