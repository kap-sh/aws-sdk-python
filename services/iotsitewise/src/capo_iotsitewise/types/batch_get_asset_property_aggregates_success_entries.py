"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesSuccessEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entry

BatchGetAssetPropertyAggregatesSuccessEntries: TypeAlias = list[
    "capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entry.BatchGetAssetPropertyAggregatesSuccessEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesSuccessEntries) -> list:
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyAggregatesSuccessEntries:
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entry

    out: BatchGetAssetPropertyAggregatesSuccessEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entry.deserialize_json(
                item
            )
        )
    return out
