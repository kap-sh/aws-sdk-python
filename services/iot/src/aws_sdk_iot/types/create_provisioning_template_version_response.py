"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningTemplateVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.is_default_version
    import aws_sdk_iot.types.template_arn
    import aws_sdk_iot.types.template_name
    import aws_sdk_iot.types.template_version_id


class CreateProvisioningTemplateVersionResponse(TypedDict, closed=True):
    template_arn: NotRequired["aws_sdk_iot.types.template_arn.TemplateArn"]
    """<p>The ARN that identifies the provisioning template.</p>"""
    template_name: NotRequired["aws_sdk_iot.types.template_name.TemplateName"]
    """<p>The name of the provisioning template.</p>"""
    version_id: NotRequired["aws_sdk_iot.types.template_version_id.TemplateVersionId"]
    """<p>The version of the provisioning template.</p>"""
    is_default_version: "aws_sdk_iot.types.is_default_version.IsDefaultVersion"
    """<p>True if the provisioning template version is the default version, otherwise false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningTemplateVersionResponse) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    out["isDefaultVersion"] = value.get("is_default_version", False)
    return out


def deserialize_json(data: dict) -> CreateProvisioningTemplateVersionResponse:
    out: CreateProvisioningTemplateVersionResponse = {}  # type: ignore[typeddict-item]
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    if "isDefaultVersion" in data:
        out["is_default_version"] = data["isDefaultVersion"]
    else:
        out["is_default_version"] = False
    return out
