"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnUpdateTemplateProvider``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cfn_stack_update_parameters
    import aws_sdk_sagemaker.types.cfn_template_name
    import aws_sdk_sagemaker.types.cfn_template_url


class CfnUpdateTemplateProvider(TypedDict):
    template_name: NotRequired[
        "aws_sdk_sagemaker.types.cfn_template_name.CfnTemplateName"
    ]
    """<p> The unique identifier of the template to update within the project. </p>"""
    template_url: NotRequired["aws_sdk_sagemaker.types.cfn_template_url.CfnTemplateURL"]
    """<p> The Amazon S3 URL of the CloudFormation template.</p>"""
    parameters: NotRequired[
        "aws_sdk_sagemaker.types.cfn_stack_update_parameters.CfnStackUpdateParameters"
    ]
    """<p> An array of CloudFormation stack parameters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnUpdateTemplateProvider) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_url" in value:
        out["TemplateURL"] = value["template_url"]
    if "parameters" in value:
        import aws_sdk_sagemaker.types.cfn_stack_update_parameters

        out["Parameters"] = (
            aws_sdk_sagemaker.types.cfn_stack_update_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CfnUpdateTemplateProvider:
    out: CfnUpdateTemplateProvider = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateURL" in data:
        out["template_url"] = data["TemplateURL"]
    if "Parameters" in data:
        import aws_sdk_sagemaker.types.cfn_stack_update_parameters

        out["parameters"] = (
            aws_sdk_sagemaker.types.cfn_stack_update_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
