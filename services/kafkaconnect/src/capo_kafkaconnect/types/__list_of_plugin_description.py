"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfPluginDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafkaconnect.types.plugin_description

__listOfPluginDescription: TypeAlias = list[
    "capo_kafkaconnect.types.plugin_description.PluginDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPluginDescription) -> list:
    import capo_kafkaconnect.types.plugin_description

    out: list = []
    for item in value:
        out.append(capo_kafkaconnect.types.plugin_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPluginDescription:
    import capo_kafkaconnect.types.plugin_description

    out: __listOfPluginDescription = []
    for item in data:
        out.append(capo_kafkaconnect.types.plugin_description.deserialize_json(item))
    return out
