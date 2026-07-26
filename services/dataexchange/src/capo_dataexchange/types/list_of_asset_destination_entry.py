"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfAssetDestinationEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.asset_destination_entry

ListOfAssetDestinationEntry: TypeAlias = list[
    "capo_dataexchange.types.asset_destination_entry.AssetDestinationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfAssetDestinationEntry) -> list:
    import capo_dataexchange.types.asset_destination_entry

    out: list = []
    for item in value:
        out.append(capo_dataexchange.types.asset_destination_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfAssetDestinationEntry:
    import capo_dataexchange.types.asset_destination_entry

    out: ListOfAssetDestinationEntry = []
    for item in data:
        out.append(
            capo_dataexchange.types.asset_destination_entry.deserialize_json(item)
        )
    return out
