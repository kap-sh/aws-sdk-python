"""Generated from Smithy shape ``com.amazonaws.sagemaker#DriftCheckBaselines``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.drift_check_bias
    import capo_sagemaker.types.drift_check_explainability
    import capo_sagemaker.types.drift_check_model_data_quality
    import capo_sagemaker.types.drift_check_model_quality


class DriftCheckBaselines(TypedDict, closed=True):
    bias: NotRequired["capo_sagemaker.types.drift_check_bias.DriftCheckBias"]
    """<p>Represents the drift check bias baselines that can be used when the model monitor is set using the model package. </p>"""
    explainability: NotRequired[
        "capo_sagemaker.types.drift_check_explainability.DriftCheckExplainability"
    ]
    """<p>Represents the drift check explainability baselines that can be used when the model monitor is set using the model package. </p>"""
    model_quality: NotRequired[
        "capo_sagemaker.types.drift_check_model_quality.DriftCheckModelQuality"
    ]
    """<p>Represents the drift check model quality baselines that can be used when the model monitor is set using the model package.</p>"""
    model_data_quality: NotRequired[
        "capo_sagemaker.types.drift_check_model_data_quality.DriftCheckModelDataQuality"
    ]
    """<p>Represents the drift check model data quality baselines that can be used when the model monitor is set using the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DriftCheckBaselines) -> dict:
    out: dict = {}
    if "bias" in value:
        import capo_sagemaker.types.drift_check_bias

        out["Bias"] = capo_sagemaker.types.drift_check_bias.serialize_aws_json_1_1(
            value["bias"]
        )
    if "explainability" in value:
        import capo_sagemaker.types.drift_check_explainability

        out["Explainability"] = (
            capo_sagemaker.types.drift_check_explainability.serialize_aws_json_1_1(
                value["explainability"]
            )
        )
    if "model_quality" in value:
        import capo_sagemaker.types.drift_check_model_quality

        out["ModelQuality"] = (
            capo_sagemaker.types.drift_check_model_quality.serialize_aws_json_1_1(
                value["model_quality"]
            )
        )
    if "model_data_quality" in value:
        import capo_sagemaker.types.drift_check_model_data_quality

        out["ModelDataQuality"] = (
            capo_sagemaker.types.drift_check_model_data_quality.serialize_aws_json_1_1(
                value["model_data_quality"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DriftCheckBaselines:
    out: DriftCheckBaselines = {}  # type: ignore[typeddict-item]
    if "Bias" in data:
        import capo_sagemaker.types.drift_check_bias

        out["bias"] = capo_sagemaker.types.drift_check_bias.deserialize_aws_json_1_1(
            data["Bias"]
        )
    if "Explainability" in data:
        import capo_sagemaker.types.drift_check_explainability

        out["explainability"] = (
            capo_sagemaker.types.drift_check_explainability.deserialize_aws_json_1_1(
                data["Explainability"]
            )
        )
    if "ModelQuality" in data:
        import capo_sagemaker.types.drift_check_model_quality

        out["model_quality"] = (
            capo_sagemaker.types.drift_check_model_quality.deserialize_aws_json_1_1(
                data["ModelQuality"]
            )
        )
    if "ModelDataQuality" in data:
        import capo_sagemaker.types.drift_check_model_data_quality

        out["model_data_quality"] = (
            capo_sagemaker.types.drift_check_model_data_quality.deserialize_aws_json_1_1(
                data["ModelDataQuality"]
            )
        )
    return out
