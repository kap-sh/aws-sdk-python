"""Generated from Smithy shape ``com.amazonaws.greengrass#GetResourceDefinitionVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.resource_definition_version


class GetResourceDefinitionVersionResponse(TypedDict, closed=True):
    arn: NotRequired["capo_greengrass.types.__string.__string"]
    """Arn of the resource definition version."""
    creation_timestamp: NotRequired["capo_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the resource definition version was created."""
    definition: NotRequired[
        "capo_greengrass.types.resource_definition_version.ResourceDefinitionVersion"
    ]
    """Information about the definition."""
    id: NotRequired["capo_greengrass.types.__string.__string"]
    """The ID of the resource definition version."""
    version: NotRequired["capo_greengrass.types.__string.__string"]
    """The version of the resource definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceDefinitionVersionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    if "definition" in value:
        import capo_greengrass.types.resource_definition_version

        out["Definition"] = (
            capo_greengrass.types.resource_definition_version.serialize_json(
                value["definition"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> GetResourceDefinitionVersionResponse:
    out: GetResourceDefinitionVersionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationTimestamp" in data:
        out["creation_timestamp"] = data["CreationTimestamp"]
    if "Definition" in data:
        import capo_greengrass.types.resource_definition_version

        out["definition"] = (
            capo_greengrass.types.resource_definition_version.deserialize_json(
                data["Definition"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
