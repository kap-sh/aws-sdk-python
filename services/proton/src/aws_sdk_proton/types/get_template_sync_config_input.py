"""Generated from Smithy shape ``com.amazonaws.proton#GetTemplateSyncConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_type


class GetTemplateSyncConfigInput(TypedDict, closed=True):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The template name.</p>"""
    template_type: "aws_sdk_proton.types.template_type.TemplateType"
    """<p>The template type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTemplateSyncConfigInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["templateType"] = value["template_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTemplateSyncConfigInput:
    out: GetTemplateSyncConfigInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("GetTemplateSyncConfigInput.template_name required")
    if "templateType" in data:
        out["template_type"] = data["templateType"]
    else:
        raise DeserializationError("GetTemplateSyncConfigInput.template_type required")
    return out
