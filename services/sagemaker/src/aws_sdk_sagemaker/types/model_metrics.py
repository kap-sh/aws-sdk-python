"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.bias
    import aws_sdk_sagemaker.types.explainability
    import aws_sdk_sagemaker.types.model_data_quality
    import aws_sdk_sagemaker.types.model_quality


class ModelMetrics(TypedDict):
    model_quality: NotRequired["aws_sdk_sagemaker.types.model_quality.ModelQuality"]
    """<p>Metrics that measure the quality of a model.</p>"""
    model_data_quality: NotRequired[
        "aws_sdk_sagemaker.types.model_data_quality.ModelDataQuality"
    ]
    """<p>Metrics that measure the quality of the input data for a model.</p>"""
    bias: NotRequired["aws_sdk_sagemaker.types.bias.Bias"]
    """<p>Metrics that measure bias in a model.</p>"""
    explainability: NotRequired["aws_sdk_sagemaker.types.explainability.Explainability"]
    """<p>Metrics that help explain a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetrics) -> dict:
    out: dict = {}
    if "model_quality" in value:
        import aws_sdk_sagemaker.types.model_quality

        out["ModelQuality"] = (
            aws_sdk_sagemaker.types.model_quality.serialize_aws_json_1_1(
                value["model_quality"]
            )
        )
    if "model_data_quality" in value:
        import aws_sdk_sagemaker.types.model_data_quality

        out["ModelDataQuality"] = (
            aws_sdk_sagemaker.types.model_data_quality.serialize_aws_json_1_1(
                value["model_data_quality"]
            )
        )
    if "bias" in value:
        import aws_sdk_sagemaker.types.bias

        out["Bias"] = aws_sdk_sagemaker.types.bias.serialize_aws_json_1_1(value["bias"])
    if "explainability" in value:
        import aws_sdk_sagemaker.types.explainability

        out["Explainability"] = (
            aws_sdk_sagemaker.types.explainability.serialize_aws_json_1_1(
                value["explainability"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelMetrics:
    out: ModelMetrics = {}  # type: ignore[typeddict-item]
    if "ModelQuality" in data:
        import aws_sdk_sagemaker.types.model_quality

        out["model_quality"] = (
            aws_sdk_sagemaker.types.model_quality.deserialize_aws_json_1_1(
                data["ModelQuality"]
            )
        )
    if "ModelDataQuality" in data:
        import aws_sdk_sagemaker.types.model_data_quality

        out["model_data_quality"] = (
            aws_sdk_sagemaker.types.model_data_quality.deserialize_aws_json_1_1(
                data["ModelDataQuality"]
            )
        )
    if "Bias" in data:
        import aws_sdk_sagemaker.types.bias

        out["bias"] = aws_sdk_sagemaker.types.bias.deserialize_aws_json_1_1(
            data["Bias"]
        )
    if "Explainability" in data:
        import aws_sdk_sagemaker.types.explainability

        out["explainability"] = (
            aws_sdk_sagemaker.types.explainability.deserialize_aws_json_1_1(
                data["Explainability"]
            )
        )
    return out
