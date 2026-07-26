"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entry

BatchGetAssetPropertyAggregatesErrorEntries: TypeAlias = list[
    "capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entry.BatchGetAssetPropertyAggregatesErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesErrorEntries) -> list:
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyAggregatesErrorEntries:
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entry

    out: BatchGetAssetPropertyAggregatesErrorEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entry.deserialize_json(
                item
            )
        )
    return out
