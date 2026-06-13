"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_summary

ConfiguredTableSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.configured_table_summary.ConfiguredTableSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableSummaryList) -> list:
    import aws_sdk_cleanrooms.types.configured_table_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfiguredTableSummaryList:
    import aws_sdk_cleanrooms.types.configured_table_summary

    out: ConfiguredTableSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_summary.deserialize_json(item)
        )
    return out
