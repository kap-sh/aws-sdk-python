"""Generated from Smithy shape ``com.amazonaws.iot#DescribeManagedJobTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.document_parameters
    import aws_sdk_iot.types.environments
    import aws_sdk_iot.types.job_description
    import aws_sdk_iot.types.job_document
    import aws_sdk_iot.types.job_template_arn
    import aws_sdk_iot.types.managed_job_template_name
    import aws_sdk_iot.types.managed_template_version


class DescribeManagedJobTemplateResponse(TypedDict):
    template_name: NotRequired[
        "aws_sdk_iot.types.managed_job_template_name.ManagedJobTemplateName"
    ]
    """<p>The unique name of a managed template, such as <code>AWS-Reboot</code>.</p>"""
    template_arn: NotRequired["aws_sdk_iot.types.job_template_arn.JobTemplateArn"]
    """<p>The unique Amazon Resource Name (ARN) of the managed template.</p>"""
    description: NotRequired["aws_sdk_iot.types.job_description.JobDescription"]
    """<p>The unique description of a managed template.</p>"""
    template_version: NotRequired[
        "aws_sdk_iot.types.managed_template_version.ManagedTemplateVersion"
    ]
    """<p>The version for a managed template.</p>"""
    environments: NotRequired["aws_sdk_iot.types.environments.Environments"]
    """<p>A list of environments that are supported with the managed job template.</p>"""
    document_parameters: NotRequired[
        "aws_sdk_iot.types.document_parameters.DocumentParameters"
    ]
    """<p>A map of key-value pairs that you can use as guidance to specify the inputs for creating a job from a managed template.</p> <note> <p> <code>documentParameters</code> can only be used when creating jobs from Amazon Web Services managed templates. This parameter can't be used with custom job templates or to create jobs from them.</p> </note>"""
    document: NotRequired["aws_sdk_iot.types.job_document.JobDocument"]
    """<p>The document schema for a managed job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeManagedJobTemplateResponse) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "template_version" in value:
        out["templateVersion"] = value["template_version"]
    if "environments" in value:
        import aws_sdk_iot.types.environments

        out["environments"] = aws_sdk_iot.types.environments.serialize_json(
            value["environments"]
        )
    if "document_parameters" in value:
        import aws_sdk_iot.types.document_parameters

        out["documentParameters"] = (
            aws_sdk_iot.types.document_parameters.serialize_json(
                value["document_parameters"]
            )
        )
    if "document" in value:
        out["document"] = value["document"]
    return out


def deserialize_json(data: dict) -> DescribeManagedJobTemplateResponse:
    out: DescribeManagedJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "templateVersion" in data:
        out["template_version"] = data["templateVersion"]
    if "environments" in data:
        import aws_sdk_iot.types.environments

        out["environments"] = aws_sdk_iot.types.environments.deserialize_json(
            data["environments"]
        )
    if "documentParameters" in data:
        import aws_sdk_iot.types.document_parameters

        out["document_parameters"] = (
            aws_sdk_iot.types.document_parameters.deserialize_json(
                data["documentParameters"]
            )
        )
    if "document" in data:
        out["document"] = data["document"]
    return out
