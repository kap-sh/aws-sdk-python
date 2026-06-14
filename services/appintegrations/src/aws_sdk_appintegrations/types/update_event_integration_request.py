"""Generated from Smithy shape ``com.amazonaws.appintegrations#UpdateEventIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.name

class UpdateEventIntegrationRequest(TypedDict):
    name: "aws_sdk_appintegrations.types.name.Name"
    """<p>The name of the event integration.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>The description of the event integration.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventIntegrationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateEventIntegrationRequest:
    out: UpdateEventIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out