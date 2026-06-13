"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginTypeMetadataSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.plugin_type_metadata_summary

ListPluginTypeMetadataSummaries: TypeAlias = list[
    "aws_sdk_qbusiness.types.plugin_type_metadata_summary.PluginTypeMetadataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginTypeMetadataSummaries) -> list:
    import aws_sdk_qbusiness.types.plugin_type_metadata_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qbusiness.types.plugin_type_metadata_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListPluginTypeMetadataSummaries:
    import aws_sdk_qbusiness.types.plugin_type_metadata_summary

    out: ListPluginTypeMetadataSummaries = []
    for item in data:
        out.append(
            aws_sdk_qbusiness.types.plugin_type_metadata_summary.deserialize_json(item)
        )
    return out
