"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.template_arn
    import capo_iot.types.template_name
    import capo_iot.types.template_version_id


class CreateProvisioningTemplateResponse(TypedDict, closed=True):
    template_arn: NotRequired["capo_iot.types.template_arn.TemplateArn"]
    """<p>The ARN that identifies the provisioning template.</p>"""
    template_name: NotRequired["capo_iot.types.template_name.TemplateName"]
    """<p>The name of the provisioning template.</p>"""
    default_version_id: NotRequired[
        "capo_iot.types.template_version_id.TemplateVersionId"
    ]
    """<p>The default version of the provisioning template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningTemplateResponse) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "default_version_id" in value:
        out["defaultVersionId"] = value["default_version_id"]
    return out


def deserialize_json(data: dict) -> CreateProvisioningTemplateResponse:
    out: CreateProvisioningTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "defaultVersionId" in data:
        out["default_version_id"] = data["defaultVersionId"]
    return out
