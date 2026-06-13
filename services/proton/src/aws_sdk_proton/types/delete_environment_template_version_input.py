"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentTemplateVersionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_version_part


class DeleteEnvironmentTemplateVersionInput(TypedDict):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template.</p>"""
    major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>The environment template major version to delete.</p>"""
    minor_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>The environment template minor version to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentTemplateVersionInput:
    out: DeleteEnvironmentTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "DeleteEnvironmentTemplateVersionInput.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "DeleteEnvironmentTemplateVersionInput.major_version required"
        )
    if "minorVersion" in data:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "DeleteEnvironmentTemplateVersionInput.minor_version required"
        )
    return out
