"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ResourceReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.name
    import aws_sdk_lex_model_building_service.types.version


class ResourceReference(TypedDict):
    name: NotRequired["aws_sdk_lex_model_building_service.types.name.Name"]
    """<p>The name of the resource that is using the resource that you are trying to delete.</p>"""
    version: NotRequired["aws_sdk_lex_model_building_service.types.version.Version"]
    """<p>The version of the resource that is using the resource that you are trying to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ResourceReference:
    out: ResourceReference = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    return out
