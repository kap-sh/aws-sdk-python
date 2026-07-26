"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.id
    import capo_appconfig.types.name


class UpdateApplicationRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The name of the application.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
