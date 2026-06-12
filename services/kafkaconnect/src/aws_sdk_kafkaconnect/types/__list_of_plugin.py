"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfPlugin``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.plugin

__listOfPlugin: TypeAlias = list["aws_sdk_kafkaconnect.types.plugin.Plugin"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPlugin) -> list:
    import aws_sdk_kafkaconnect.types.plugin

    out: list = []
    for item in value:
        out.append(aws_sdk_kafkaconnect.types.plugin.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPlugin:
    import aws_sdk_kafkaconnect.types.plugin

    out: __listOfPlugin = []
    for item in data:
        out.append(aws_sdk_kafkaconnect.types.plugin.deserialize_json(item))
    return out
