"""Generated from Smithy shape ``com.amazonaws.greengrass#Logger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__integer
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.logger_component
    import aws_sdk_greengrass.types.logger_level
    import aws_sdk_greengrass.types.logger_type


class Logger(TypedDict, closed=True):
    component: NotRequired["aws_sdk_greengrass.types.logger_component.LoggerComponent"]
    """The component that will be subject to logging."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''."""
    level: NotRequired["aws_sdk_greengrass.types.logger_level.LoggerLevel"]
    """The level of the logs."""
    space: NotRequired["aws_sdk_greengrass.types.__integer.__integer"]
    """The amount of file space, in KB, to use if the local file system is used for logging purposes."""
    type: NotRequired["aws_sdk_greengrass.types.logger_type.LoggerType"]
    """The type of log output which will be used."""


# --- restJson1 ser/de ---
def serialize_json(value: Logger) -> dict:
    out: dict = {}
    if "component" in value:
        import aws_sdk_greengrass.types.logger_component

        out["Component"] = aws_sdk_greengrass.types.logger_component.serialize_json(
            value["component"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "level" in value:
        import aws_sdk_greengrass.types.logger_level

        out["Level"] = aws_sdk_greengrass.types.logger_level.serialize_json(
            value["level"]
        )
    if "space" in value:
        out["Space"] = value["space"]
    if "type" in value:
        import aws_sdk_greengrass.types.logger_type

        out["Type"] = aws_sdk_greengrass.types.logger_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Logger:
    out: Logger = {}  # type: ignore[typeddict-item]
    if "Component" in data:
        import aws_sdk_greengrass.types.logger_component

        out["component"] = aws_sdk_greengrass.types.logger_component.deserialize_json(
            data["Component"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Level" in data:
        import aws_sdk_greengrass.types.logger_level

        out["level"] = aws_sdk_greengrass.types.logger_level.deserialize_json(
            data["Level"]
        )
    if "Space" in data:
        out["space"] = data["Space"]
    if "Type" in data:
        import aws_sdk_greengrass.types.logger_type

        out["type"] = aws_sdk_greengrass.types.logger_type.deserialize_json(
            data["Type"]
        )
    return out
