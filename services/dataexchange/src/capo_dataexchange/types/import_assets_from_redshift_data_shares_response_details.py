"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetsFromRedshiftDataSharesResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.id
    import capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry


class ImportAssetsFromRedshiftDataSharesResponseDetails(TypedDict, closed=True):
    asset_sources: "capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry.ListOfRedshiftDataShareAssetSourceEntry"
    """<p>A list of Amazon Redshift datashare asset sources.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetsFromRedshiftDataSharesResponseDetails) -> dict:
    out: dict = {}
    import capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry

    out["AssetSources"] = (
        capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry.serialize_json(
            value["asset_sources"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ImportAssetsFromRedshiftDataSharesResponseDetails:
    out: ImportAssetsFromRedshiftDataSharesResponseDetails = {}  # type: ignore[typeddict-item]
    if "AssetSources" in data:
        import capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry

        out["asset_sources"] = (
            capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry.deserialize_json(
                data["AssetSources"]
            )
        )
    else:
        raise DeserializationError(
            "ImportAssetsFromRedshiftDataSharesResponseDetails.asset_sources required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ImportAssetsFromRedshiftDataSharesResponseDetails.data_set_id required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ImportAssetsFromRedshiftDataSharesResponseDetails.revision_id required"
        )
    return out
