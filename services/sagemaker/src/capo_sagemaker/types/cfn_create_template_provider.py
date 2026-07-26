"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnCreateTemplateProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cfn_stack_create_parameters
    import capo_sagemaker.types.cfn_template_name
    import capo_sagemaker.types.cfn_template_url
    import capo_sagemaker.types.role_arn


class CfnCreateTemplateProvider(TypedDict, closed=True):
    template_name: NotRequired["capo_sagemaker.types.cfn_template_name.CfnTemplateName"]
    """<p> A unique identifier for the template within the project. </p>"""
    template_url: NotRequired["capo_sagemaker.types.cfn_template_url.CfnTemplateURL"]
    """<p> The Amazon S3 URL of the CloudFormation template. </p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p> The IAM role that CloudFormation assumes when creating the stack. </p>"""
    parameters: NotRequired[
        "capo_sagemaker.types.cfn_stack_create_parameters.CfnStackCreateParameters"
    ]
    """<p> An array of CloudFormation stack parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnCreateTemplateProvider) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_url" in value:
        out["TemplateURL"] = value["template_url"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "parameters" in value:
        import capo_sagemaker.types.cfn_stack_create_parameters

        out["Parameters"] = (
            capo_sagemaker.types.cfn_stack_create_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CfnCreateTemplateProvider:
    out: CfnCreateTemplateProvider = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateURL" in data:
        out["template_url"] = data["TemplateURL"]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "Parameters" in data:
        import capo_sagemaker.types.cfn_stack_create_parameters

        out["parameters"] = (
            capo_sagemaker.types.cfn_stack_create_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
