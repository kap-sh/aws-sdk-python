"""Generated from Smithy shape ``com.amazonaws.sagemaker#DriftCheckBaselines``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.drift_check_bias
    import aws_sdk_sagemaker.types.drift_check_explainability
    import aws_sdk_sagemaker.types.drift_check_model_data_quality
    import aws_sdk_sagemaker.types.drift_check_model_quality


class DriftCheckBaselines(TypedDict, closed=True):
    bias: NotRequired["aws_sdk_sagemaker.types.drift_check_bias.DriftCheckBias"]
    """<p>Represents the drift check bias baselines that can be used when the model monitor is set using the model package. </p>"""
    explainability: NotRequired[
        "aws_sdk_sagemaker.types.drift_check_explainability.DriftCheckExplainability"
    ]
    """<p>Represents the drift check explainability baselines that can be used when the model monitor is set using the model package. </p>"""
    model_quality: NotRequired[
        "aws_sdk_sagemaker.types.drift_check_model_quality.DriftCheckModelQuality"
    ]
    """<p>Represents the drift check model quality baselines that can be used when the model monitor is set using the model package.</p>"""
    model_data_quality: NotRequired[
        "aws_sdk_sagemaker.types.drift_check_model_data_quality.DriftCheckModelDataQuality"
    ]
    """<p>Represents the drift check model data quality baselines that can be used when the model monitor is set using the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DriftCheckBaselines) -> dict:
    out: dict = {}
    if "bias" in value:
        import aws_sdk_sagemaker.types.drift_check_bias

        out["Bias"] = aws_sdk_sagemaker.types.drift_check_bias.serialize_aws_json_1_1(
            value["bias"]
        )
    if "explainability" in value:
        import aws_sdk_sagemaker.types.drift_check_explainability

        out["Explainability"] = (
            aws_sdk_sagemaker.types.drift_check_explainability.serialize_aws_json_1_1(
                value["explainability"]
            )
        )
    if "model_quality" in value:
        import aws_sdk_sagemaker.types.drift_check_model_quality

        out["ModelQuality"] = (
            aws_sdk_sagemaker.types.drift_check_model_quality.serialize_aws_json_1_1(
                value["model_quality"]
            )
        )
    if "model_data_quality" in value:
        import aws_sdk_sagemaker.types.drift_check_model_data_quality

        out["ModelDataQuality"] = (
            aws_sdk_sagemaker.types.drift_check_model_data_quality.serialize_aws_json_1_1(
                value["model_data_quality"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DriftCheckBaselines:
    out: DriftCheckBaselines = {}  # type: ignore[typeddict-item]
    if "Bias" in data:
        import aws_sdk_sagemaker.types.drift_check_bias

        out["bias"] = aws_sdk_sagemaker.types.drift_check_bias.deserialize_aws_json_1_1(
            data["Bias"]
        )
    if "Explainability" in data:
        import aws_sdk_sagemaker.types.drift_check_explainability

        out["explainability"] = (
            aws_sdk_sagemaker.types.drift_check_explainability.deserialize_aws_json_1_1(
                data["Explainability"]
            )
        )
    if "ModelQuality" in data:
        import aws_sdk_sagemaker.types.drift_check_model_quality

        out["model_quality"] = (
            aws_sdk_sagemaker.types.drift_check_model_quality.deserialize_aws_json_1_1(
                data["ModelQuality"]
            )
        )
    if "ModelDataQuality" in data:
        import aws_sdk_sagemaker.types.drift_check_model_data_quality

        out["model_data_quality"] = (
            aws_sdk_sagemaker.types.drift_check_model_data_quality.deserialize_aws_json_1_1(
                data["ModelDataQuality"]
            )
        )
    return out
