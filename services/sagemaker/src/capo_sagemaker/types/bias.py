"""Generated from Smithy shape ``com.amazonaws.sagemaker#Bias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.metrics_source


class Bias(TypedDict, closed=True):
    report: NotRequired["capo_sagemaker.types.metrics_source.MetricsSource"]
    """<p>The bias report for a model</p>"""
    pre_training_report: NotRequired[
        "capo_sagemaker.types.metrics_source.MetricsSource"
    ]
    """<p>The pre-training bias report for a model.</p>"""
    post_training_report: NotRequired[
        "capo_sagemaker.types.metrics_source.MetricsSource"
    ]
    """<p>The post-training bias report for a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Bias) -> dict:
    out: dict = {}
    if "report" in value:
        import capo_sagemaker.types.metrics_source

        out["Report"] = capo_sagemaker.types.metrics_source.serialize_aws_json_1_1(
            value["report"]
        )
    if "pre_training_report" in value:
        import capo_sagemaker.types.metrics_source

        out["PreTrainingReport"] = (
            capo_sagemaker.types.metrics_source.serialize_aws_json_1_1(
                value["pre_training_report"]
            )
        )
    if "post_training_report" in value:
        import capo_sagemaker.types.metrics_source

        out["PostTrainingReport"] = (
            capo_sagemaker.types.metrics_source.serialize_aws_json_1_1(
                value["post_training_report"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Bias:
    out: Bias = {}  # type: ignore[typeddict-item]
    if "Report" in data:
        import capo_sagemaker.types.metrics_source

        out["report"] = capo_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
            data["Report"]
        )
    if "PreTrainingReport" in data:
        import capo_sagemaker.types.metrics_source

        out["pre_training_report"] = (
            capo_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["PreTrainingReport"]
            )
        )
    if "PostTrainingReport" in data:
        import capo_sagemaker.types.metrics_source

        out["post_training_report"] = (
            capo_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["PostTrainingReport"]
            )
        )
    return out
