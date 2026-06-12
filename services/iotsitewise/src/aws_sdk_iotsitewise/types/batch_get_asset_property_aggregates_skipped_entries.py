"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesSkippedEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entry

BatchGetAssetPropertyAggregatesSkippedEntries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entry.BatchGetAssetPropertyAggregatesSkippedEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesSkippedEntries) -> list:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyAggregatesSkippedEntries:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entry

    out: BatchGetAssetPropertyAggregatesSkippedEntries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entry.deserialize_json(
                item
            )
        )
    return out
