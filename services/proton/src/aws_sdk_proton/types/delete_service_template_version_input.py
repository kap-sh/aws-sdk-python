"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceTemplateVersionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_version_part


class DeleteServiceTemplateVersionInput(TypedDict):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>The service template major version to delete.</p>"""
    minor_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>The service template minor version to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceTemplateVersionInput:
    out: DeleteServiceTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "DeleteServiceTemplateVersionInput.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "DeleteServiceTemplateVersionInput.major_version required"
        )
    if "minorVersion" in data:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "DeleteServiceTemplateVersionInput.minor_version required"
        )
    return out
