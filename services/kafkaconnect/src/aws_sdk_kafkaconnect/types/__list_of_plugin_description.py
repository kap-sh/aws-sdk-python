"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfPluginDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.plugin_description

__listOfPluginDescription: TypeAlias = list[
    "aws_sdk_kafkaconnect.types.plugin_description.PluginDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPluginDescription) -> list:
    import aws_sdk_kafkaconnect.types.plugin_description

    out: list = []
    for item in value:
        out.append(aws_sdk_kafkaconnect.types.plugin_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPluginDescription:
    import aws_sdk_kafkaconnect.types.plugin_description

    out: __listOfPluginDescription = []
    for item in data:
        out.append(aws_sdk_kafkaconnect.types.plugin_description.deserialize_json(item))
    return out
