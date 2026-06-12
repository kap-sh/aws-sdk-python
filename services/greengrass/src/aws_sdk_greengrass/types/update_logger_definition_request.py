"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateLoggerDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class UpdateLoggerDefinitionRequest(TypedDict):
    logger_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the logger definition."""
    name: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the definition."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLoggerDefinitionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateLoggerDefinitionRequest:
    out: UpdateLoggerDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
