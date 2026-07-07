"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricDatum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_metric_enum
    import aws_sdk_sagemaker.types.auto_ml_metric_extended_enum
    import aws_sdk_sagemaker.types.float
    import aws_sdk_sagemaker.types.metric_set_source


class MetricDatum(TypedDict, closed=True):
    metric_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_metric_enum.AutoMLMetricEnum"
    ]
    """<p>The name of the metric.</p>"""
    standard_metric_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_metric_extended_enum.AutoMLMetricExtendedEnum"
    ]
    r"""<p>The name of the standard metric. </p> <note> <p>For definitions of the standard metrics, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-metrics\"> <code>Autopilot candidate metrics</code> </a>.</p> </note>"""
    value: NotRequired["aws_sdk_sagemaker.types.float.Float"]
    """<p>The value of the metric.</p>"""
    set: NotRequired["aws_sdk_sagemaker.types.metric_set_source.MetricSetSource"]
    """<p>The dataset split from which the AutoML job produced the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDatum) -> dict:
    out: dict = {}
    if "metric_name" in value:
        import aws_sdk_sagemaker.types.auto_ml_metric_enum

        out["MetricName"] = (
            aws_sdk_sagemaker.types.auto_ml_metric_enum.serialize_aws_json_1_1(
                value["metric_name"]
            )
        )
    if "standard_metric_name" in value:
        import aws_sdk_sagemaker.types.auto_ml_metric_extended_enum

        out["StandardMetricName"] = (
            aws_sdk_sagemaker.types.auto_ml_metric_extended_enum.serialize_aws_json_1_1(
                value["standard_metric_name"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    if "set" in value:
        import aws_sdk_sagemaker.types.metric_set_source

        out["Set"] = aws_sdk_sagemaker.types.metric_set_source.serialize_aws_json_1_1(
            value["set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDatum:
    out: MetricDatum = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        import aws_sdk_sagemaker.types.auto_ml_metric_enum

        out["metric_name"] = (
            aws_sdk_sagemaker.types.auto_ml_metric_enum.deserialize_aws_json_1_1(
                data["MetricName"]
            )
        )
    if "StandardMetricName" in data:
        import aws_sdk_sagemaker.types.auto_ml_metric_extended_enum

        out["standard_metric_name"] = (
            aws_sdk_sagemaker.types.auto_ml_metric_extended_enum.deserialize_aws_json_1_1(
                data["StandardMetricName"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    if "Set" in data:
        import aws_sdk_sagemaker.types.metric_set_source

        out["set"] = aws_sdk_sagemaker.types.metric_set_source.deserialize_aws_json_1_1(
            data["Set"]
        )
    return out
