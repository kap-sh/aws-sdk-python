"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTemplateProvider``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cfn_update_template_provider


class UpdateTemplateProvider(TypedDict):
    cfn_template_provider: NotRequired[
        "aws_sdk_sagemaker.types.cfn_update_template_provider.CfnUpdateTemplateProvider"
    ]
    """<p> The CloudFormation template provider configuration to update. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTemplateProvider) -> dict:
    out: dict = {}
    if "cfn_template_provider" in value:
        import aws_sdk_sagemaker.types.cfn_update_template_provider

        out["CfnTemplateProvider"] = (
            aws_sdk_sagemaker.types.cfn_update_template_provider.serialize_aws_json_1_1(
                value["cfn_template_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTemplateProvider:
    out: UpdateTemplateProvider = {}  # type: ignore[typeddict-item]
    if "CfnTemplateProvider" in data:
        import aws_sdk_sagemaker.types.cfn_update_template_provider

        out["cfn_template_provider"] = (
            aws_sdk_sagemaker.types.cfn_update_template_provider.deserialize_aws_json_1_1(
                data["CfnTemplateProvider"]
            )
        )
    return out
