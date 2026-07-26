"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateLoggerDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_logger
    import capo_greengrass.types.__string


class CreateLoggerDefinitionVersionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    logger_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the logger definition."""
    loggers: NotRequired["capo_greengrass.types.__list_of_logger.__listOfLogger"]
    """A list of loggers."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLoggerDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "loggers" in value:
        import capo_greengrass.types.__list_of_logger

        out["Loggers"] = capo_greengrass.types.__list_of_logger.serialize_json(
            value["loggers"]
        )
    return out


def deserialize_json(data: dict) -> CreateLoggerDefinitionVersionRequest:
    out: CreateLoggerDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Loggers" in data:
        import capo_greengrass.types.__list_of_logger

        out["loggers"] = capo_greengrass.types.__list_of_logger.deserialize_json(
            data["Loggers"]
        )
    return out
