"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceTemplateVersionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_version_part


class GetServiceTemplateVersionInput(TypedDict):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template a version of which you want to get detailed data for.</p>"""
    major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>To get service template major version detail data, include <code>major Version</code>.</p>"""
    minor_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>To get service template minor version detail data, include <code>minorVersion</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceTemplateVersionInput:
    out: GetServiceTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "GetServiceTemplateVersionInput.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "GetServiceTemplateVersionInput.major_version required"
        )
    if "minorVersion" in data:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "GetServiceTemplateVersionInput.minor_version required"
        )
    return out
