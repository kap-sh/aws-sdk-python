"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfPlugin``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafkaconnect.types.plugin

__listOfPlugin: TypeAlias = list["capo_kafkaconnect.types.plugin.Plugin"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPlugin) -> list:
    import capo_kafkaconnect.types.plugin

    out: list = []
    for item in value:
        out.append(capo_kafkaconnect.types.plugin.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPlugin:
    import capo_kafkaconnect.types.plugin

    out: __listOfPlugin = []
    for item in data:
        out.append(capo_kafkaconnect.types.plugin.deserialize_json(item))
    return out
