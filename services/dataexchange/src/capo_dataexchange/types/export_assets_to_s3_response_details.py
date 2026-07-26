"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportAssetsToS3ResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.export_server_side_encryption
    import capo_dataexchange.types.id
    import capo_dataexchange.types.list_of_asset_destination_entry


class ExportAssetsToS3ResponseDetails(TypedDict, closed=True):
    asset_destinations: "capo_dataexchange.types.list_of_asset_destination_entry.ListOfAssetDestinationEntry"
    """<p>The destination in Amazon S3 where the asset is exported.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    encryption: NotRequired[
        "capo_dataexchange.types.export_server_side_encryption.ExportServerSideEncryption"
    ]
    """<p>Encryption configuration of the export job.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this export response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAssetsToS3ResponseDetails) -> dict:
    out: dict = {}
    import capo_dataexchange.types.list_of_asset_destination_entry

    out["AssetDestinations"] = (
        capo_dataexchange.types.list_of_asset_destination_entry.serialize_json(
            value["asset_destinations"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    if "encryption" in value:
        import capo_dataexchange.types.export_server_side_encryption

        out["Encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.serialize_json(
                value["encryption"]
            )
        )
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ExportAssetsToS3ResponseDetails:
    out: ExportAssetsToS3ResponseDetails = {}  # type: ignore[typeddict-item]
    if "AssetDestinations" in data:
        import capo_dataexchange.types.list_of_asset_destination_entry

        out["asset_destinations"] = (
            capo_dataexchange.types.list_of_asset_destination_entry.deserialize_json(
                data["AssetDestinations"]
            )
        )
    else:
        raise DeserializationError(
            "ExportAssetsToS3ResponseDetails.asset_destinations required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ExportAssetsToS3ResponseDetails.data_set_id required"
        )
    if "Encryption" in data:
        import capo_dataexchange.types.export_server_side_encryption

        out["encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.deserialize_json(
                data["Encryption"]
            )
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ExportAssetsToS3ResponseDetails.revision_id required"
        )
    return out
