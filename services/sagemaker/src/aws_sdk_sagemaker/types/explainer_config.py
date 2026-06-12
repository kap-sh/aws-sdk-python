"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExplainerConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.clarify_explainer_config


class ExplainerConfig(TypedDict):
    clarify_explainer_config: NotRequired[
        "aws_sdk_sagemaker.types.clarify_explainer_config.ClarifyExplainerConfig"
    ]
    """<p>A member of <code>ExplainerConfig</code> that contains configuration parameters for the SageMaker Clarify explainer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplainerConfig) -> dict:
    out: dict = {}
    if "clarify_explainer_config" in value:
        import aws_sdk_sagemaker.types.clarify_explainer_config

        out["ClarifyExplainerConfig"] = (
            aws_sdk_sagemaker.types.clarify_explainer_config.serialize_aws_json_1_1(
                value["clarify_explainer_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExplainerConfig:
    out: ExplainerConfig = {}  # type: ignore[typeddict-item]
    if "ClarifyExplainerConfig" in data:
        import aws_sdk_sagemaker.types.clarify_explainer_config

        out["clarify_explainer_config"] = (
            aws_sdk_sagemaker.types.clarify_explainer_config.deserialize_aws_json_1_1(
                data["ClarifyExplainerConfig"]
            )
        )
    return out
