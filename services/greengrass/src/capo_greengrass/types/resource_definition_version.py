"""Generated from Smithy shape ``com.amazonaws.greengrass#ResourceDefinitionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_resource


class ResourceDefinitionVersion(TypedDict, closed=True):
    resources: NotRequired["capo_greengrass.types.__list_of_resource.__listOfResource"]
    """A list of resources."""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDefinitionVersion) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_greengrass.types.__list_of_resource

        out["Resources"] = capo_greengrass.types.__list_of_resource.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> ResourceDefinitionVersion:
    out: ResourceDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import capo_greengrass.types.__list_of_resource

        out["resources"] = capo_greengrass.types.__list_of_resource.deserialize_json(
            data["Resources"]
        )
    return out
