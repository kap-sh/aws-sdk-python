"""Generated from Smithy shape ``com.amazonaws.greengrass#GetResourceDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetResourceDefinitionVersionRequest(TypedDict, closed=True):
    resource_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the resource definition."""
    resource_definition_version_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the resource definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListResourceDefinitionVersions'' requests. If the version is the last one that was associated with a resource definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object."""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceDefinitionVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceDefinitionVersionRequest:
    out: GetResourceDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    return out
