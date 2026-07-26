"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerDefinitionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_logger


class LoggerDefinitionVersion(TypedDict, closed=True):
    loggers: NotRequired["capo_greengrass.types.__list_of_logger.__listOfLogger"]
    """A list of loggers."""


# --- restJson1 ser/de ---
def serialize_json(value: LoggerDefinitionVersion) -> dict:
    out: dict = {}
    if "loggers" in value:
        import capo_greengrass.types.__list_of_logger

        out["Loggers"] = capo_greengrass.types.__list_of_logger.serialize_json(
            value["loggers"]
        )
    return out


def deserialize_json(data: dict) -> LoggerDefinitionVersion:
    out: LoggerDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Loggers" in data:
        import capo_greengrass.types.__list_of_logger

        out["loggers"] = capo_greengrass.types.__list_of_logger.deserialize_json(
            data["Loggers"]
        )
    return out
