"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfCustomPluginSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafkaconnect.types.custom_plugin_summary

__listOfCustomPluginSummary: TypeAlias = list[
    "capo_kafkaconnect.types.custom_plugin_summary.CustomPluginSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCustomPluginSummary) -> list:
    import capo_kafkaconnect.types.custom_plugin_summary

    out: list = []
    for item in value:
        out.append(capo_kafkaconnect.types.custom_plugin_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCustomPluginSummary:
    import capo_kafkaconnect.types.custom_plugin_summary

    out: __listOfCustomPluginSummary = []
    for item in data:
        out.append(capo_kafkaconnect.types.custom_plugin_summary.deserialize_json(item))
    return out
