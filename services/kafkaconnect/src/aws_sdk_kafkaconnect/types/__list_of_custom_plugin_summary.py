"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfCustomPluginSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.custom_plugin_summary

__listOfCustomPluginSummary: TypeAlias = list[
    "aws_sdk_kafkaconnect.types.custom_plugin_summary.CustomPluginSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCustomPluginSummary) -> list:
    import aws_sdk_kafkaconnect.types.custom_plugin_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kafkaconnect.types.custom_plugin_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCustomPluginSummary:
    import aws_sdk_kafkaconnect.types.custom_plugin_summary

    out: __listOfCustomPluginSummary = []
    for item in data:
        out.append(
            aws_sdk_kafkaconnect.types.custom_plugin_summary.deserialize_json(item)
        )
    return out
