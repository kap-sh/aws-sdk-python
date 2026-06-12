"""Generated from Smithy shape ``com.amazonaws.mq#__listOfConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.configuration

__listOfConfiguration: TypeAlias = list["aws_sdk_mq.types.configuration.Configuration"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConfiguration) -> list:
    import aws_sdk_mq.types.configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConfiguration:
    import aws_sdk_mq.types.configuration

    out: __listOfConfiguration = []
    for item in data:
        out.append(aws_sdk_mq.types.configuration.deserialize_json(item))
    return out
