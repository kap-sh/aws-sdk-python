"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateLoggerDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.logger_definition_version
    import capo_greengrass.types.tags


class CreateLoggerDefinitionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    initial_version: NotRequired[
        "capo_greengrass.types.logger_definition_version.LoggerDefinitionVersion"
    ]
    """Information about the initial version of the logger definition."""
    name: NotRequired["capo_greengrass.types.__string.__string"]
    """The name of the logger definition."""
    tags: NotRequired["capo_greengrass.types.tags.Tags"]
    """Tag(s) to add to the new resource."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLoggerDefinitionRequest) -> dict:
    out: dict = {}
    if "initial_version" in value:
        import capo_greengrass.types.logger_definition_version

        out["InitialVersion"] = (
            capo_greengrass.types.logger_definition_version.serialize_json(
                value["initial_version"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "tags" in value:
        import capo_greengrass.types.tags

        out["tags"] = capo_greengrass.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateLoggerDefinitionRequest:
    out: CreateLoggerDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "InitialVersion" in data:
        import capo_greengrass.types.logger_definition_version

        out["initial_version"] = (
            capo_greengrass.types.logger_definition_version.deserialize_json(
                data["InitialVersion"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "tags" in data:
        import capo_greengrass.types.tags

        out["tags"] = capo_greengrass.types.tags.deserialize_json(data["tags"])
    return out
