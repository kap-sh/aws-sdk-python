"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfRedshiftDataShareAssetSourceEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.redshift_data_share_asset_source_entry

ListOfRedshiftDataShareAssetSourceEntry: TypeAlias = list[
    "capo_dataexchange.types.redshift_data_share_asset_source_entry.RedshiftDataShareAssetSourceEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRedshiftDataShareAssetSourceEntry) -> list:
    import capo_dataexchange.types.redshift_data_share_asset_source_entry

    out: list = []
    for item in value:
        out.append(
            capo_dataexchange.types.redshift_data_share_asset_source_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfRedshiftDataShareAssetSourceEntry:
    import capo_dataexchange.types.redshift_data_share_asset_source_entry

    out: ListOfRedshiftDataShareAssetSourceEntry = []
    for item in data:
        out.append(
            capo_dataexchange.types.redshift_data_share_asset_source_entry.deserialize_json(
                item
            )
        )
    return out
