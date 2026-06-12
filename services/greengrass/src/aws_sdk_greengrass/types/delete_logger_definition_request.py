"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteLoggerDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class DeleteLoggerDefinitionRequest(TypedDict):
    logger_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the logger definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLoggerDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLoggerDefinitionRequest:
    out: DeleteLoggerDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
