"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTemplateProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cfn_update_template_provider


class UpdateTemplateProvider(TypedDict, closed=True):
    cfn_template_provider: NotRequired[
        "capo_sagemaker.types.cfn_update_template_provider.CfnUpdateTemplateProvider"
    ]
    """<p> The CloudFormation template provider configuration to update. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTemplateProvider) -> dict:
    out: dict = {}
    if "cfn_template_provider" in value:
        import capo_sagemaker.types.cfn_update_template_provider

        out["CfnTemplateProvider"] = (
            capo_sagemaker.types.cfn_update_template_provider.serialize_aws_json_1_1(
                value["cfn_template_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTemplateProvider:
    out: UpdateTemplateProvider = {}  # type: ignore[typeddict-item]
    if "CfnTemplateProvider" in data:
        import capo_sagemaker.types.cfn_update_template_provider

        out["cfn_template_provider"] = (
            capo_sagemaker.types.cfn_update_template_provider.deserialize_aws_json_1_1(
                data["CfnTemplateProvider"]
            )
        )
    return out
