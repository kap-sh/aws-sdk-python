"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningTemplateVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.set_as_default
    import aws_sdk_iot.types.template_body
    import aws_sdk_iot.types.template_name


class CreateProvisioningTemplateVersionRequest(TypedDict):
    template_name: "aws_sdk_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template.</p>"""
    template_body: "aws_sdk_iot.types.template_body.TemplateBody"
    """<p>The JSON formatted contents of the provisioning template.</p>"""
    set_as_default: "aws_sdk_iot.types.set_as_default.SetAsDefault"
    """<p>Sets a fleet provision template version as the default version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningTemplateVersionRequest) -> dict:
    out: dict = {}
    out["templateBody"] = value["template_body"]
    return out


def deserialize_json(data: dict) -> CreateProvisioningTemplateVersionRequest:
    out: CreateProvisioningTemplateVersionRequest = {}  # type: ignore[typeddict-item]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    else:
        raise DeserializationError(
            "CreateProvisioningTemplateVersionRequest.template_body required"
        )
    return out
