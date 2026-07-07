"""Generated from Smithy shape ``com.amazonaws.proton#GetTemplateSyncStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_type
    import aws_sdk_proton.types.template_version_part


class GetTemplateSyncStatusInput(TypedDict, closed=True):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The template name.</p>"""
    template_type: "aws_sdk_proton.types.template_type.TemplateType"
    """<p>The template type.</p>"""
    template_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>The template major version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTemplateSyncStatusInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["templateType"] = value["template_type"]
    out["templateVersion"] = value["template_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTemplateSyncStatusInput:
    out: GetTemplateSyncStatusInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("GetTemplateSyncStatusInput.template_name required")
    if "templateType" in data:
        out["template_type"] = data["templateType"]
    else:
        raise DeserializationError("GetTemplateSyncStatusInput.template_type required")
    if "templateVersion" in data:
        out["template_version"] = data["templateVersion"]
    else:
        raise DeserializationError(
            "GetTemplateSyncStatusInput.template_version required"
        )
    return out
