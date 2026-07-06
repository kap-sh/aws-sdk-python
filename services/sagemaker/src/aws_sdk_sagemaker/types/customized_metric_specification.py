"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomizedMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.statistic
    import aws_sdk_sagemaker.types.string


class CustomizedMetricSpecification(TypedDict, closed=True):
    metric_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the customized metric.</p>"""
    namespace: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The namespace of the customized metric.</p>"""
    statistic: NotRequired["aws_sdk_sagemaker.types.statistic.Statistic"]
    """<p>The statistic of the customized metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizedMetricSpecification) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "statistic" in value:
        import aws_sdk_sagemaker.types.statistic

        out["Statistic"] = aws_sdk_sagemaker.types.statistic.serialize_aws_json_1_1(
            value["statistic"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomizedMetricSpecification:
    out: CustomizedMetricSpecification = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "Statistic" in data:
        import aws_sdk_sagemaker.types.statistic

        out["statistic"] = aws_sdk_sagemaker.types.statistic.deserialize_aws_json_1_1(
            data["Statistic"]
        )
    return out
