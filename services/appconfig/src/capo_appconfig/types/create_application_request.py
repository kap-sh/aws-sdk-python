"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.name
    import capo_appconfig.types.tag_map


class CreateApplicationRequest(TypedDict, closed=True):
    name: "capo_appconfig.types.name.Name"
    """<p>A name for the application.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the application.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to the application. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
