"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTemplateProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cfn_create_template_provider


class CreateTemplateProvider(TypedDict, closed=True):
    cfn_template_provider: NotRequired[
        "capo_sagemaker.types.cfn_create_template_provider.CfnCreateTemplateProvider"
    ]
    """<p> The CloudFormation template provider configuration for creating infrastructure resources. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTemplateProvider) -> dict:
    out: dict = {}
    if "cfn_template_provider" in value:
        import capo_sagemaker.types.cfn_create_template_provider

        out["CfnTemplateProvider"] = (
            capo_sagemaker.types.cfn_create_template_provider.serialize_aws_json_1_1(
                value["cfn_template_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTemplateProvider:
    out: CreateTemplateProvider = {}  # type: ignore[typeddict-item]
    if "CfnTemplateProvider" in data:
        import capo_sagemaker.types.cfn_create_template_provider

        out["cfn_template_provider"] = (
            capo_sagemaker.types.cfn_create_template_provider.deserialize_aws_json_1_1(
                data["CfnTemplateProvider"]
            )
        )
    return out
