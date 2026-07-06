"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportAssetsToS3RequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.export_server_side_encryption
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.list_of_asset_destination_entry


class ExportAssetsToS3RequestDetails(TypedDict, closed=True):
    asset_destinations: "aws_sdk_dataexchange.types.list_of_asset_destination_entry.ListOfAssetDestinationEntry"
    """<p>The destination for the asset.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    encryption: NotRequired[
        "aws_sdk_dataexchange.types.export_server_side_encryption.ExportServerSideEncryption"
    ]
    """<p>Encryption configuration for the export job.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this export request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAssetsToS3RequestDetails) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.list_of_asset_destination_entry

    out["AssetDestinations"] = (
        aws_sdk_dataexchange.types.list_of_asset_destination_entry.serialize_json(
            value["asset_destinations"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    if "encryption" in value:
        import aws_sdk_dataexchange.types.export_server_side_encryption

        out["Encryption"] = (
            aws_sdk_dataexchange.types.export_server_side_encryption.serialize_json(
                value["encryption"]
            )
        )
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ExportAssetsToS3RequestDetails:
    out: ExportAssetsToS3RequestDetails = {}  # type: ignore[typeddict-item]
    if "AssetDestinations" in data:
        import aws_sdk_dataexchange.types.list_of_asset_destination_entry

        out["asset_destinations"] = (
            aws_sdk_dataexchange.types.list_of_asset_destination_entry.deserialize_json(
                data["AssetDestinations"]
            )
        )
    else:
        raise DeserializationError(
            "ExportAssetsToS3RequestDetails.asset_destinations required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ExportAssetsToS3RequestDetails.data_set_id required"
        )
    if "Encryption" in data:
        import aws_sdk_dataexchange.types.export_server_side_encryption

        out["encryption"] = (
            aws_sdk_dataexchange.types.export_server_side_encryption.deserialize_json(
                data["Encryption"]
            )
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ExportAssetsToS3RequestDetails.revision_id required"
        )
    return out
