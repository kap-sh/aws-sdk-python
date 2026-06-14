"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyShapConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.clarify_shap_baseline_config
    import aws_sdk_sagemaker.types.clarify_shap_number_of_samples
    import aws_sdk_sagemaker.types.clarify_shap_seed
    import aws_sdk_sagemaker.types.clarify_shap_use_logit
    import aws_sdk_sagemaker.types.clarify_text_config


class ClarifyShapConfig(TypedDict):
    shap_baseline_config: NotRequired[
        "aws_sdk_sagemaker.types.clarify_shap_baseline_config.ClarifyShapBaselineConfig"
    ]
    """<p>The configuration for the SHAP baseline of the Kernal SHAP algorithm.</p>"""
    number_of_samples: NotRequired[
        "aws_sdk_sagemaker.types.clarify_shap_number_of_samples.ClarifyShapNumberOfSamples"
    ]
    r"""<p>The number of samples to be used for analysis by the Kernal SHAP algorithm. </p> <note> <p>The number of samples determines the size of the synthetic dataset, which has an impact on latency of explainability requests. For more information, see the <b>Synthetic data</b> of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html\">Configure and create an endpoint</a>.</p> </note>"""
    use_logit: NotRequired[
        "aws_sdk_sagemaker.types.clarify_shap_use_logit.ClarifyShapUseLogit"
    ]
    """<p>A Boolean toggle to indicate if you want to use the logit function (true) or log-odds units (false) for model predictions. Defaults to false.</p>"""
    seed: NotRequired["aws_sdk_sagemaker.types.clarify_shap_seed.ClarifyShapSeed"]
    """<p>The starting value used to initialize the random number generator in the explainer. Provide a value for this parameter to obtain a deterministic SHAP result.</p>"""
    text_config: NotRequired[
        "aws_sdk_sagemaker.types.clarify_text_config.ClarifyTextConfig"
    ]
    """<p>A parameter that indicates if text features are treated as text and explanations are provided for individual units of text. Required for natural language processing (NLP) explainability only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyShapConfig) -> dict:
    out: dict = {}
    if "shap_baseline_config" in value:
        import aws_sdk_sagemaker.types.clarify_shap_baseline_config

        out["ShapBaselineConfig"] = (
            aws_sdk_sagemaker.types.clarify_shap_baseline_config.serialize_aws_json_1_1(
                value["shap_baseline_config"]
            )
        )
    if "number_of_samples" in value:
        out["NumberOfSamples"] = value["number_of_samples"]
    if "use_logit" in value:
        out["UseLogit"] = value["use_logit"]
    if "seed" in value:
        out["Seed"] = value["seed"]
    if "text_config" in value:
        import aws_sdk_sagemaker.types.clarify_text_config

        out["TextConfig"] = (
            aws_sdk_sagemaker.types.clarify_text_config.serialize_aws_json_1_1(
                value["text_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClarifyShapConfig:
    out: ClarifyShapConfig = {}  # type: ignore[typeddict-item]
    if "ShapBaselineConfig" in data:
        import aws_sdk_sagemaker.types.clarify_shap_baseline_config

        out["shap_baseline_config"] = (
            aws_sdk_sagemaker.types.clarify_shap_baseline_config.deserialize_aws_json_1_1(
                data["ShapBaselineConfig"]
            )
        )
    if "NumberOfSamples" in data:
        out["number_of_samples"] = data["NumberOfSamples"]
    if "UseLogit" in data:
        out["use_logit"] = data["UseLogit"]
    if "Seed" in data:
        out["seed"] = data["Seed"]
    if "TextConfig" in data:
        import aws_sdk_sagemaker.types.clarify_text_config

        out["text_config"] = (
            aws_sdk_sagemaker.types.clarify_text_config.deserialize_aws_json_1_1(
                data["TextConfig"]
            )
        )
    return out
