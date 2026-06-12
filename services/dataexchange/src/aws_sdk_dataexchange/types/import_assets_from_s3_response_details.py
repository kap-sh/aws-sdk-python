"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetsFromS3ResponseDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.list_of_asset_source_entry


class ImportAssetsFromS3ResponseDetails(TypedDict):
    asset_sources: (
        "aws_sdk_dataexchange.types.list_of_asset_source_entry.ListOfAssetSourceEntry"
    )
    """<p>Is a list of Amazon S3 bucket and object key pairs.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetsFromS3ResponseDetails) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.list_of_asset_source_entry

    out["AssetSources"] = (
        aws_sdk_dataexchange.types.list_of_asset_source_entry.serialize_json(
            value["asset_sources"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ImportAssetsFromS3ResponseDetails:
    out: ImportAssetsFromS3ResponseDetails = {}  # type: ignore[typeddict-item]
    if "AssetSources" in data:
        import aws_sdk_dataexchange.types.list_of_asset_source_entry

        out["asset_sources"] = (
            aws_sdk_dataexchange.types.list_of_asset_source_entry.deserialize_json(
                data["AssetSources"]
            )
        )
    else:
        raise DeserializationError(
            "ImportAssetsFromS3ResponseDetails.asset_sources required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ImportAssetsFromS3ResponseDetails.data_set_id required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ImportAssetsFromS3ResponseDetails.revision_id required"
        )
    return out
