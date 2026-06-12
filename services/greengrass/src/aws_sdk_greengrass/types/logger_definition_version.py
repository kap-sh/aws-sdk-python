"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerDefinitionVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_logger


class LoggerDefinitionVersion(TypedDict):
    loggers: NotRequired["aws_sdk_greengrass.types.__list_of_logger.__listOfLogger"]
    """A list of loggers."""


# --- restJson1 ser/de ---
def serialize_json(value: LoggerDefinitionVersion) -> dict:
    out: dict = {}
    if "loggers" in value:
        import aws_sdk_greengrass.types.__list_of_logger

        out["Loggers"] = aws_sdk_greengrass.types.__list_of_logger.serialize_json(
            value["loggers"]
        )
    return out


def deserialize_json(data: dict) -> LoggerDefinitionVersion:
    out: LoggerDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Loggers" in data:
        import aws_sdk_greengrass.types.__list_of_logger

        out["loggers"] = aws_sdk_greengrass.types.__list_of_logger.deserialize_json(
            data["Loggers"]
        )
    return out
