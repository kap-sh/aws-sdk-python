"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.display_name
    import aws_sdk_proton.types.resource_name


class UpdateServiceTemplateInput(TypedDict, closed=True):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template to update.</p>"""
    display_name: NotRequired["aws_sdk_proton.types.display_name.DisplayName"]
    """<p>The name of the service template to update that's displayed in the developer interface.</p>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>A description of the service template update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceTemplateInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceTemplateInput:
    out: UpdateServiceTemplateInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateServiceTemplateInput.name required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    return out
