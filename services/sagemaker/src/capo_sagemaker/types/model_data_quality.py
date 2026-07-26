"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDataQuality``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.metrics_source


class ModelDataQuality(TypedDict, closed=True):
    statistics: NotRequired["capo_sagemaker.types.metrics_source.MetricsSource"]
    """<p>Data quality statistics for a model.</p>"""
    constraints: NotRequired["capo_sagemaker.types.metrics_source.MetricsSource"]
    """<p>Data quality constraints for a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDataQuality) -> dict:
    out: dict = {}
    if "statistics" in value:
        import capo_sagemaker.types.metrics_source

        out["Statistics"] = capo_sagemaker.types.metrics_source.serialize_aws_json_1_1(
            value["statistics"]
        )
    if "constraints" in value:
        import capo_sagemaker.types.metrics_source

        out["Constraints"] = capo_sagemaker.types.metrics_source.serialize_aws_json_1_1(
            value["constraints"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDataQuality:
    out: ModelDataQuality = {}  # type: ignore[typeddict-item]
    if "Statistics" in data:
        import capo_sagemaker.types.metrics_source

        out["statistics"] = (
            capo_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    if "Constraints" in data:
        import capo_sagemaker.types.metrics_source

        out["constraints"] = (
            capo_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["Constraints"]
            )
        )
    return out
