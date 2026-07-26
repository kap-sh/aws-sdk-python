"""Generated from Smithy shape ``com.amazonaws.proton#CompatibleEnvironmentTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.resource_name
    import capo_proton.types.template_version_part


class CompatibleEnvironmentTemplateInput(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The compatible environment template name.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The major version of the compatible environment template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompatibleEnvironmentTemplateInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CompatibleEnvironmentTemplateInput:
    out: CompatibleEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "CompatibleEnvironmentTemplateInput.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "CompatibleEnvironmentTemplateInput.major_version required"
        )
    return out
