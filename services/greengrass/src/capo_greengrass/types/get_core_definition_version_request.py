"""Generated from Smithy shape ``com.amazonaws.greengrass#GetCoreDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class GetCoreDefinitionVersionRequest(TypedDict, closed=True):
    core_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the core definition."""
    core_definition_version_id: "capo_greengrass.types.__string.__string"
    """The ID of the core definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListCoreDefinitionVersions'' requests. If the version is the last one that was associated with a core definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreDefinitionVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCoreDefinitionVersionRequest:
    out: GetCoreDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    return out
