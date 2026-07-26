"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfAssetEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.asset_entry

ListOfAssetEntry: TypeAlias = list["capo_dataexchange.types.asset_entry.AssetEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfAssetEntry) -> list:
    import capo_dataexchange.types.asset_entry

    out: list = []
    for item in value:
        out.append(capo_dataexchange.types.asset_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfAssetEntry:
    import capo_dataexchange.types.asset_entry

    out: ListOfAssetEntry = []
    for item in data:
        out.append(capo_dataexchange.types.asset_entry.deserialize_json(item))
    return out
