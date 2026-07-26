"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateS3DataAccessFromS3BucketRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.id
    import capo_dataexchange.types.s3_data_access_asset_source_entry


class CreateS3DataAccessFromS3BucketRequestDetails(TypedDict, closed=True):
    asset_source: "capo_dataexchange.types.s3_data_access_asset_source_entry.S3DataAccessAssetSourceEntry"
    """<p>Details about the S3 data access source asset.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with the creation of this Amazon S3 data access.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateS3DataAccessFromS3BucketRequestDetails) -> dict:
    out: dict = {}
    import capo_dataexchange.types.s3_data_access_asset_source_entry

    out["AssetSource"] = (
        capo_dataexchange.types.s3_data_access_asset_source_entry.serialize_json(
            value["asset_source"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> CreateS3DataAccessFromS3BucketRequestDetails:
    out: CreateS3DataAccessFromS3BucketRequestDetails = {}  # type: ignore[typeddict-item]
    if "AssetSource" in data:
        import capo_dataexchange.types.s3_data_access_asset_source_entry

        out["asset_source"] = (
            capo_dataexchange.types.s3_data_access_asset_source_entry.deserialize_json(
                data["AssetSource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateS3DataAccessFromS3BucketRequestDetails.asset_source required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "CreateS3DataAccessFromS3BucketRequestDetails.data_set_id required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "CreateS3DataAccessFromS3BucketRequestDetails.revision_id required"
        )
    return out
