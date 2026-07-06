"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteAnomalyDetectorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.anomaly_detector_metric_stat
    import aws_sdk_cloudwatch.types.dimensions
    import aws_sdk_cloudwatch.types.metric_math_anomaly_detector
    import aws_sdk_cloudwatch.types.metric_name
    import aws_sdk_cloudwatch.types.namespace
    import aws_sdk_cloudwatch.types.single_metric_anomaly_detector


class DeleteAnomalyDetectorInput(TypedDict, closed=True):
    namespace: NotRequired["aws_sdk_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace associated with the anomaly detection model to delete.</p>"""
    metric_name: NotRequired["aws_sdk_cloudwatch.types.metric_name.MetricName"]
    """<p>The metric name associated with the anomaly detection model to delete.</p>"""
    dimensions: NotRequired["aws_sdk_cloudwatch.types.dimensions.Dimensions"]
    """<p>The metric dimensions associated with the anomaly detection model to delete.</p>"""
    stat: NotRequired[
        "aws_sdk_cloudwatch.types.anomaly_detector_metric_stat.AnomalyDetectorMetricStat"
    ]
    """<p>The statistic associated with the anomaly detection model to delete.</p>"""
    single_metric_anomaly_detector: NotRequired[
        "aws_sdk_cloudwatch.types.single_metric_anomaly_detector.SingleMetricAnomalyDetector"
    ]
    """<p>A single metric anomaly detector to be deleted.</p> <p>When using <code>SingleMetricAnomalyDetector</code>, you cannot include the following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code>,</p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>MetricMathAnomalyDetector</code> parameters of <code>DeleteAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the single metric anomaly detector attributes as part of the <code>SingleMetricAnomalyDetector</code> property.</p>"""
    metric_math_anomaly_detector: NotRequired[
        "aws_sdk_cloudwatch.types.metric_math_anomaly_detector.MetricMathAnomalyDetector"
    ]
    """<p>The metric math anomaly detector to be deleted.</p> <p>When using <code>MetricMathAnomalyDetector</code>, you cannot include following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code>,</p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>SingleMetricAnomalyDetector</code> parameters of <code>DeleteAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the metric math anomaly detector attributes as part of the <code>MetricMathAnomalyDetector</code> property.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAnomalyDetectorInput) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import aws_sdk_cloudwatch.types.dimensions

        out["Dimensions"] = aws_sdk_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "stat" in value:
        out["Stat"] = value["stat"]
    if "single_metric_anomaly_detector" in value:
        import aws_sdk_cloudwatch.types.single_metric_anomaly_detector

        out["SingleMetricAnomalyDetector"] = (
            aws_sdk_cloudwatch.types.single_metric_anomaly_detector.serialize_aws_json_1_0(
                value["single_metric_anomaly_detector"]
            )
        )
    if "metric_math_anomaly_detector" in value:
        import aws_sdk_cloudwatch.types.metric_math_anomaly_detector

        out["MetricMathAnomalyDetector"] = (
            aws_sdk_cloudwatch.types.metric_math_anomaly_detector.serialize_aws_json_1_0(
                value["metric_math_anomaly_detector"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAnomalyDetectorInput:
    out: DeleteAnomalyDetectorInput = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Dimensions" in data:
        import aws_sdk_cloudwatch.types.dimensions

        out["dimensions"] = (
            aws_sdk_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    if "Stat" in data:
        out["stat"] = data["Stat"]
    if "SingleMetricAnomalyDetector" in data:
        import aws_sdk_cloudwatch.types.single_metric_anomaly_detector

        out["single_metric_anomaly_detector"] = (
            aws_sdk_cloudwatch.types.single_metric_anomaly_detector.deserialize_aws_json_1_0(
                data["SingleMetricAnomalyDetector"]
            )
        )
    if "MetricMathAnomalyDetector" in data:
        import aws_sdk_cloudwatch.types.metric_math_anomaly_detector

        out["metric_math_anomaly_detector"] = (
            aws_sdk_cloudwatch.types.metric_math_anomaly_detector.deserialize_aws_json_1_0(
                data["MetricMathAnomalyDetector"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAnomalyDetectorInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "namespace" in value:
        pairs.append((f"{prefix}.Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{prefix}.MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import aws_sdk_cloudwatch.types.dimensions

        aws_sdk_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{prefix}.Dimensions"
        )
    if "stat" in value:
        pairs.append((f"{prefix}.Stat", str(value["stat"])))
    if "single_metric_anomaly_detector" in value:
        import aws_sdk_cloudwatch.types.single_metric_anomaly_detector

        aws_sdk_cloudwatch.types.single_metric_anomaly_detector.serialize_query(
            value["single_metric_anomaly_detector"],
            pairs,
            f"{prefix}.SingleMetricAnomalyDetector",
        )
    if "metric_math_anomaly_detector" in value:
        import aws_sdk_cloudwatch.types.metric_math_anomaly_detector

        aws_sdk_cloudwatch.types.metric_math_anomaly_detector.serialize_query(
            value["metric_math_anomaly_detector"],
            pairs,
            f"{prefix}.MetricMathAnomalyDetector",
        )


def deserialize_query(el: Element) -> DeleteAnomalyDetectorInput:
    out: DeleteAnomalyDetectorInput = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import aws_sdk_cloudwatch.types.dimensions

        out["dimensions"] = aws_sdk_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    child_stat = el.find("Stat")
    if child_stat is not None:
        out["stat"] = str(child_stat.text or "")
    child_single_metric_anomaly_detector = el.find("SingleMetricAnomalyDetector")
    if child_single_metric_anomaly_detector is not None:
        import aws_sdk_cloudwatch.types.single_metric_anomaly_detector

        out["single_metric_anomaly_detector"] = (
            aws_sdk_cloudwatch.types.single_metric_anomaly_detector.deserialize_query(
                child_single_metric_anomaly_detector
            )
        )
    child_metric_math_anomaly_detector = el.find("MetricMathAnomalyDetector")
    if child_metric_math_anomaly_detector is not None:
        import aws_sdk_cloudwatch.types.metric_math_anomaly_detector

        out["metric_math_anomaly_detector"] = (
            aws_sdk_cloudwatch.types.metric_math_anomaly_detector.deserialize_query(
                child_metric_math_anomaly_detector
            )
        )
    return out
