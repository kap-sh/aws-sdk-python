"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entry

BatchGetAssetPropertyAggregatesEntries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entry.BatchGetAssetPropertyAggregatesEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesEntries) -> list:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyAggregatesEntries:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entry

    out: BatchGetAssetPropertyAggregatesEntries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entry.deserialize_json(
                item
            )
        )
    return out
