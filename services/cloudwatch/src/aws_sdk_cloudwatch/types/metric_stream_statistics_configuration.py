"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamStatisticsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics
    import aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics


class MetricStreamStatisticsConfiguration(TypedDict):
    include_metrics: NotRequired[
        "aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics.MetricStreamStatisticsIncludeMetrics"
    ]
    """<p>An array of metric name and namespace pairs that stream the additional statistics listed in the value of the <code>AdditionalStatistics</code> parameter. There can be as many as 100 pairs in the array.</p> <p>All metrics that match the combination of metric name and namespace will be streamed with the additional statistics, no matter their dimensions.</p>"""
    additional_statistics: NotRequired[
        "aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics.MetricStreamStatisticsAdditionalStatistics"
    ]
    """<p>The list of additional statistics that are to be streamed for the metrics listed in the <code>IncludeMetrics</code> array in this structure. This list can include as many as 20 statistics.</p> <p>If the <code>OutputFormat</code> for the stream is <code>opentelemetry1.0</code> or <code>opentelemetry0.7</code>, the only valid values are <code>p<i>??</i> </code> percentile statistics such as <code>p90</code>, <code>p99</code> and so on.</p> <p>If the <code>OutputFormat</code> for the stream is <code>json</code>, the valid values include the abbreviations for all of the statistics listed in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html.html\"> CloudWatch statistics definitions</a>. For example, this includes <code>tm98, </code> <code>wm90</code>, <code>PR(:300)</code>, and so on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamStatisticsConfiguration) -> dict:
    out: dict = {}
    if "include_metrics" in value:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics

        out["IncludeMetrics"] = (
            aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics.serialize_aws_json_1_0(
                value["include_metrics"]
            )
        )
    if "additional_statistics" in value:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics

        out["AdditionalStatistics"] = (
            aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics.serialize_aws_json_1_0(
                value["additional_statistics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricStreamStatisticsConfiguration:
    out: MetricStreamStatisticsConfiguration = {}  # type: ignore[typeddict-item]
    if "IncludeMetrics" in data:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics

        out["include_metrics"] = (
            aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics.deserialize_aws_json_1_0(
                data["IncludeMetrics"]
            )
        )
    if "AdditionalStatistics" in data:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics

        out["additional_statistics"] = (
            aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics.deserialize_aws_json_1_0(
                data["AdditionalStatistics"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamStatisticsConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "include_metrics" in value:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics

        aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics.serialize_query(
            value["include_metrics"], pairs, f"{prefix}.IncludeMetrics"
        )
    if "additional_statistics" in value:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics

        aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics.serialize_query(
            value["additional_statistics"], pairs, f"{prefix}.AdditionalStatistics"
        )


def deserialize_query(el: Element) -> MetricStreamStatisticsConfiguration:
    out: MetricStreamStatisticsConfiguration = {}  # type: ignore[typeddict-item]
    child_include_metrics = el.find("IncludeMetrics")
    if child_include_metrics is not None:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics

        out["include_metrics"] = (
            aws_sdk_cloudwatch.types.metric_stream_statistics_include_metrics.deserialize_query(
                child_include_metrics
            )
        )
    child_additional_statistics = el.find("AdditionalStatistics")
    if child_additional_statistics is not None:
        import aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics

        out["additional_statistics"] = (
            aws_sdk_cloudwatch.types.metric_stream_statistics_additional_statistics.deserialize_query(
                child_additional_statistics
            )
        )
    return out
