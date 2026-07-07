"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionEvaluationMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.evaluation_metric
    import aws_sdk_textract.types.feature_type


class AdapterVersionEvaluationMetric(TypedDict, closed=True):
    baseline: NotRequired["aws_sdk_textract.types.evaluation_metric.EvaluationMetric"]
    """<p>The F1 score, precision, and recall metrics for the baseline model.</p>"""
    adapter_version: NotRequired[
        "aws_sdk_textract.types.evaluation_metric.EvaluationMetric"
    ]
    """<p>The F1 score, precision, and recall metrics for the baseline model.</p>"""
    feature_type: NotRequired["aws_sdk_textract.types.feature_type.FeatureType"]
    """<p>Indicates the feature type being analyzed by a given adapter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionEvaluationMetric) -> dict:
    out: dict = {}
    if "baseline" in value:
        import aws_sdk_textract.types.evaluation_metric

        out["Baseline"] = (
            aws_sdk_textract.types.evaluation_metric.serialize_aws_json_1_1(
                value["baseline"]
            )
        )
    if "adapter_version" in value:
        import aws_sdk_textract.types.evaluation_metric

        out["AdapterVersion"] = (
            aws_sdk_textract.types.evaluation_metric.serialize_aws_json_1_1(
                value["adapter_version"]
            )
        )
    if "feature_type" in value:
        import aws_sdk_textract.types.feature_type

        out["FeatureType"] = aws_sdk_textract.types.feature_type.serialize_aws_json_1_1(
            value["feature_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdapterVersionEvaluationMetric:
    out: AdapterVersionEvaluationMetric = {}  # type: ignore[typeddict-item]
    if "Baseline" in data:
        import aws_sdk_textract.types.evaluation_metric

        out["baseline"] = (
            aws_sdk_textract.types.evaluation_metric.deserialize_aws_json_1_1(
                data["Baseline"]
            )
        )
    if "AdapterVersion" in data:
        import aws_sdk_textract.types.evaluation_metric

        out["adapter_version"] = (
            aws_sdk_textract.types.evaluation_metric.deserialize_aws_json_1_1(
                data["AdapterVersion"]
            )
        )
    if "FeatureType" in data:
        import aws_sdk_textract.types.feature_type

        out["feature_type"] = (
            aws_sdk_textract.types.feature_type.deserialize_aws_json_1_1(
                data["FeatureType"]
            )
        )
    return out
