"""Generated from Smithy shape ``com.amazonaws.greengrass#GetLoggerDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class GetLoggerDefinitionVersionRequest(TypedDict, closed=True):
    logger_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the logger definition."""
    logger_definition_version_id: "capo_greengrass.types.__string.__string"
    """The ID of the logger definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListLoggerDefinitionVersions'' requests. If the version is the last one that was associated with a logger definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object."""
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: GetLoggerDefinitionVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLoggerDefinitionVersionRequest:
    out: GetLoggerDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    return out
