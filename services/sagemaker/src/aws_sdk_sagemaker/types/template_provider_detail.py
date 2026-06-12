"""Generated from Smithy shape ``com.amazonaws.sagemaker#TemplateProviderDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cfn_template_provider_detail


class TemplateProviderDetail(TypedDict):
    cfn_template_provider_detail: NotRequired[
        "aws_sdk_sagemaker.types.cfn_template_provider_detail.CfnTemplateProviderDetail"
    ]
    """<p> Details about a CloudFormation template provider configuration and associated provisioning information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TemplateProviderDetail) -> dict:
    out: dict = {}
    if "cfn_template_provider_detail" in value:
        import aws_sdk_sagemaker.types.cfn_template_provider_detail

        out["CfnTemplateProviderDetail"] = (
            aws_sdk_sagemaker.types.cfn_template_provider_detail.serialize_aws_json_1_1(
                value["cfn_template_provider_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TemplateProviderDetail:
    out: TemplateProviderDetail = {}  # type: ignore[typeddict-item]
    if "CfnTemplateProviderDetail" in data:
        import aws_sdk_sagemaker.types.cfn_template_provider_detail

        out["cfn_template_provider_detail"] = (
            aws_sdk_sagemaker.types.cfn_template_provider_detail.deserialize_aws_json_1_1(
                data["CfnTemplateProviderDetail"]
            )
        )
    return out
