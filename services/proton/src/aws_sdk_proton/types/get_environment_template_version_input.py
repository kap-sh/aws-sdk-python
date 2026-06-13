"""Generated from Smithy shape ``com.amazonaws.proton#GetEnvironmentTemplateVersionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.template_version_part


class GetEnvironmentTemplateVersionInput(TypedDict):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template a version of which you want to get detailed data for.</p>"""
    major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>To get environment template major version detail data, include <code>major Version</code>.</p>"""
    minor_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    """<p>To get environment template minor version detail data, include <code>minorVersion</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentTemplateVersionInput:
    out: GetEnvironmentTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "GetEnvironmentTemplateVersionInput.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "GetEnvironmentTemplateVersionInput.major_version required"
        )
    if "minorVersion" in data:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "GetEnvironmentTemplateVersionInput.minor_version required"
        )
    return out
