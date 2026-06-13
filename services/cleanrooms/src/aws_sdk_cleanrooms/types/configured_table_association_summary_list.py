"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_summary

ConfiguredTableAssociationSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.configured_table_association_summary.ConfiguredTableAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationSummaryList) -> list:
    import aws_sdk_cleanrooms.types.configured_table_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredTableAssociationSummaryList:
    import aws_sdk_cleanrooms.types.configured_table_association_summary

    out: ConfiguredTableAssociationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_association_summary.deserialize_json(
                item
            )
        )
    return out
