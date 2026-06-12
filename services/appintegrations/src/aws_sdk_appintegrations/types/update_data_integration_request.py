"""Generated from Smithy shape ``com.amazonaws.appintegrations#UpdateDataIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.identifier
    import aws_sdk_appintegrations.types.name


class UpdateDataIntegrationRequest(TypedDict):
    identifier: "aws_sdk_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier for the DataIntegration.</p>"""
    name: NotRequired["aws_sdk_appintegrations.types.name.Name"]
    """<p>The name of the DataIntegration.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>A description of the DataIntegration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataIntegrationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateDataIntegrationRequest:
    out: UpdateDataIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
