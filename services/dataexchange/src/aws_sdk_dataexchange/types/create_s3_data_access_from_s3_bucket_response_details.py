"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateS3DataAccessFromS3BucketResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.s3_data_access_asset_source_entry


class CreateS3DataAccessFromS3BucketResponseDetails(TypedDict, closed=True):
    asset_source: "aws_sdk_dataexchange.types.s3_data_access_asset_source_entry.S3DataAccessAssetSourceEntry"
    """<p>Details about the asset source from an Amazon S3 bucket.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for this data set.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateS3DataAccessFromS3BucketResponseDetails) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.s3_data_access_asset_source_entry

    out["AssetSource"] = (
        aws_sdk_dataexchange.types.s3_data_access_asset_source_entry.serialize_json(
            value["asset_source"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> CreateS3DataAccessFromS3BucketResponseDetails:
    out: CreateS3DataAccessFromS3BucketResponseDetails = {}  # type: ignore[typeddict-item]
    if "AssetSource" in data:
        import aws_sdk_dataexchange.types.s3_data_access_asset_source_entry

        out["asset_source"] = (
            aws_sdk_dataexchange.types.s3_data_access_asset_source_entry.deserialize_json(
                data["AssetSource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateS3DataAccessFromS3BucketResponseDetails.asset_source required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "CreateS3DataAccessFromS3BucketResponseDetails.data_set_id required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "CreateS3DataAccessFromS3BucketResponseDetails.revision_id required"
        )
    return out
