"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.bias
    import capo_sagemaker.types.explainability
    import capo_sagemaker.types.model_data_quality
    import capo_sagemaker.types.model_quality


class ModelMetrics(TypedDict, closed=True):
    model_quality: NotRequired["capo_sagemaker.types.model_quality.ModelQuality"]
    """<p>Metrics that measure the quality of a model.</p>"""
    model_data_quality: NotRequired[
        "capo_sagemaker.types.model_data_quality.ModelDataQuality"
    ]
    """<p>Metrics that measure the quality of the input data for a model.</p>"""
    bias: NotRequired["capo_sagemaker.types.bias.Bias"]
    """<p>Metrics that measure bias in a model.</p>"""
    explainability: NotRequired["capo_sagemaker.types.explainability.Explainability"]
    """<p>Metrics that help explain a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetrics) -> dict:
    out: dict = {}
    if "model_quality" in value:
        import capo_sagemaker.types.model_quality

        out["ModelQuality"] = capo_sagemaker.types.model_quality.serialize_aws_json_1_1(
            value["model_quality"]
        )
    if "model_data_quality" in value:
        import capo_sagemaker.types.model_data_quality

        out["ModelDataQuality"] = (
            capo_sagemaker.types.model_data_quality.serialize_aws_json_1_1(
                value["model_data_quality"]
            )
        )
    if "bias" in value:
        import capo_sagemaker.types.bias

        out["Bias"] = capo_sagemaker.types.bias.serialize_aws_json_1_1(value["bias"])
    if "explainability" in value:
        import capo_sagemaker.types.explainability

        out["Explainability"] = (
            capo_sagemaker.types.explainability.serialize_aws_json_1_1(
                value["explainability"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelMetrics:
    out: ModelMetrics = {}  # type: ignore[typeddict-item]
    if "ModelQuality" in data:
        import capo_sagemaker.types.model_quality

        out["model_quality"] = (
            capo_sagemaker.types.model_quality.deserialize_aws_json_1_1(
                data["ModelQuality"]
            )
        )
    if "ModelDataQuality" in data:
        import capo_sagemaker.types.model_data_quality

        out["model_data_quality"] = (
            capo_sagemaker.types.model_data_quality.deserialize_aws_json_1_1(
                data["ModelDataQuality"]
            )
        )
    if "Bias" in data:
        import capo_sagemaker.types.bias

        out["bias"] = capo_sagemaker.types.bias.deserialize_aws_json_1_1(data["Bias"])
    if "Explainability" in data:
        import capo_sagemaker.types.explainability

        out["explainability"] = (
            capo_sagemaker.types.explainability.deserialize_aws_json_1_1(
                data["Explainability"]
            )
        )
    return out
