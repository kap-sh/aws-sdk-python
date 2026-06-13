"""Generated from Smithy shape ``com.amazonaws.proton#UpdateEnvironmentTemplateVersionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_version_part
    import aws_sdk_proton.types.template_version_status


class UpdateEnvironmentTemplateVersionInput(TypedDict):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template.</p>"""
    major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>To update a major version of an environment template, include <code>major Version</code>.</p>"""
    minor_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>To update a minor version of an environment template, include <code>minorVersion</code>.</p>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>A description of environment template version to update.</p>"""
    status: NotRequired[
        "aws_sdk_proton.types.template_version_status.TemplateVersionStatus"
    ]
    """<p>The status of the environment template minor version to update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentTemplateVersionInput:
    out: UpdateEnvironmentTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentTemplateVersionInput.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentTemplateVersionInput.major_version required"
        )
    if "minorVersion" in data:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentTemplateVersionInput.minor_version required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        out["status"] = data["status"]
    return out
