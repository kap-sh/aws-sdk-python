"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetsFromRedshiftDataSharesResponseDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.list_of_redshift_data_share_asset_source_entry


class ImportAssetsFromRedshiftDataSharesResponseDetails(TypedDict):
    asset_sources: "aws_sdk_dataexchange.types.list_of_redshift_data_share_asset_source_entry.ListOfRedshiftDataShareAssetSourceEntry"
    """<p>A list of Amazon Redshift datashare asset sources.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetsFromRedshiftDataSharesResponseDetails) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.list_of_redshift_data_share_asset_source_entry

    out["AssetSources"] = (
        aws_sdk_dataexchange.types.list_of_redshift_data_share_asset_source_entry.serialize_json(
            value["asset_sources"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ImportAssetsFromRedshiftDataSharesResponseDetails:
    out: ImportAssetsFromRedshiftDataSharesResponseDetails = {}  # type: ignore[typeddict-item]
    if "AssetSources" in data:
        import aws_sdk_dataexchange.types.list_of_redshift_data_share_asset_source_entry

        out["asset_sources"] = (
            aws_sdk_dataexchange.types.list_of_redshift_data_share_asset_source_entry.deserialize_json(
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
