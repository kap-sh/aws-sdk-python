"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfAssetSourceEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.asset_source_entry

ListOfAssetSourceEntry: TypeAlias = list[
    "capo_dataexchange.types.asset_source_entry.AssetSourceEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfAssetSourceEntry) -> list:
    import capo_dataexchange.types.asset_source_entry

    out: list = []
    for item in value:
        out.append(capo_dataexchange.types.asset_source_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfAssetSourceEntry:
    import capo_dataexchange.types.asset_source_entry

    out: ListOfAssetSourceEntry = []
    for item in data:
        out.append(capo_dataexchange.types.asset_source_entry.deserialize_json(item))
    return out
