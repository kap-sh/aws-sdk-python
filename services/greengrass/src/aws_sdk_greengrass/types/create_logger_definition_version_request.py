"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateLoggerDefinitionVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_logger
    import aws_sdk_greengrass.types.__string


class CreateLoggerDefinitionVersionRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    logger_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the logger definition."""
    loggers: NotRequired["aws_sdk_greengrass.types.__list_of_logger.__listOfLogger"]
    """A list of loggers."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLoggerDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "loggers" in value:
        import aws_sdk_greengrass.types.__list_of_logger

        out["Loggers"] = aws_sdk_greengrass.types.__list_of_logger.serialize_json(
            value["loggers"]
        )
    return out


def deserialize_json(data: dict) -> CreateLoggerDefinitionVersionRequest:
    out: CreateLoggerDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Loggers" in data:
        import aws_sdk_greengrass.types.__list_of_logger

        out["loggers"] = aws_sdk_greengrass.types.__list_of_logger.deserialize_json(
            data["Loggers"]
        )
    return out
