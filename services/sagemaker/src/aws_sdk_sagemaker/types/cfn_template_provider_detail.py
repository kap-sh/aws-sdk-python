"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnTemplateProviderDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cfn_stack_detail
    import aws_sdk_sagemaker.types.cfn_stack_parameters
    import aws_sdk_sagemaker.types.cfn_template_name
    import aws_sdk_sagemaker.types.cfn_template_url
    import aws_sdk_sagemaker.types.role_arn


class CfnTemplateProviderDetail(TypedDict, closed=True):
    template_name: NotRequired[
        "aws_sdk_sagemaker.types.cfn_template_name.CfnTemplateName"
    ]
    """<p> The unique identifier of the template within the project. </p>"""
    template_url: NotRequired["aws_sdk_sagemaker.types.cfn_template_url.CfnTemplateURL"]
    """<p> The Amazon S3 URL of the CloudFormation template. </p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p> The IAM role used by CloudFormation to create the stack. </p>"""
    parameters: NotRequired[
        "aws_sdk_sagemaker.types.cfn_stack_parameters.CfnStackParameters"
    ]
    """<p> An array of CloudFormation stack parameters.</p>"""
    stack_detail: NotRequired["aws_sdk_sagemaker.types.cfn_stack_detail.CfnStackDetail"]
    """<p> Information about the CloudFormation stack created by the template provider. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnTemplateProviderDetail) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_url" in value:
        out["TemplateURL"] = value["template_url"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "parameters" in value:
        import aws_sdk_sagemaker.types.cfn_stack_parameters

        out["Parameters"] = (
            aws_sdk_sagemaker.types.cfn_stack_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "stack_detail" in value:
        import aws_sdk_sagemaker.types.cfn_stack_detail

        out["StackDetail"] = (
            aws_sdk_sagemaker.types.cfn_stack_detail.serialize_aws_json_1_1(
                value["stack_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CfnTemplateProviderDetail:
    out: CfnTemplateProviderDetail = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateURL" in data:
        out["template_url"] = data["TemplateURL"]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "Parameters" in data:
        import aws_sdk_sagemaker.types.cfn_stack_parameters

        out["parameters"] = (
            aws_sdk_sagemaker.types.cfn_stack_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "StackDetail" in data:
        import aws_sdk_sagemaker.types.cfn_stack_detail

        out["stack_detail"] = (
            aws_sdk_sagemaker.types.cfn_stack_detail.deserialize_aws_json_1_1(
                data["StackDetail"]
            )
        )
    return out
