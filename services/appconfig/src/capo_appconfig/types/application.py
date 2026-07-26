"""Generated from Smithy shape ``com.amazonaws.appconfig#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.id
    import capo_appconfig.types.name


class Application(TypedDict, closed=True):
    id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The application name.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The description of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
