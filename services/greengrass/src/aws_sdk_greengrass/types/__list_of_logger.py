"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfLogger``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.logger

__listOfLogger: TypeAlias = list["aws_sdk_greengrass.types.logger.Logger"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfLogger) -> list:
    import aws_sdk_greengrass.types.logger

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.logger.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfLogger:
    import aws_sdk_greengrass.types.logger

    out: __listOfLogger = []
    for item in data:
        out.append(aws_sdk_greengrass.types.logger.deserialize_json(item))
    return out
