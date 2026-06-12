"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportAssetToSignedUrlResponseDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.timestamp


class ExportAssetToSignedUrlResponseDetails(TypedDict):
    asset_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the asset associated with this export job.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this export response.</p>"""
    signed_url: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The signed URL for the export request.</p>"""
    signed_url_expires_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the signed URL expires, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAssetToSignedUrlResponseDetails) -> dict:
    out: dict = {}
    out["AssetId"] = value["asset_id"]
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    if "signed_url" in value:
        out["SignedUrl"] = value["signed_url"]
    if "signed_url_expires_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["SignedUrlExpiresAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["signed_url_expires_at"]
        )
    return out


def deserialize_json(data: dict) -> ExportAssetToSignedUrlResponseDetails:
    out: ExportAssetToSignedUrlResponseDetails = {}  # type: ignore[typeddict-item]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    else:
        raise DeserializationError(
            "ExportAssetToSignedUrlResponseDetails.asset_id required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ExportAssetToSignedUrlResponseDetails.data_set_id required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ExportAssetToSignedUrlResponseDetails.revision_id required"
        )
    if "SignedUrl" in data:
        out["signed_url"] = data["SignedUrl"]
    if "SignedUrlExpiresAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["signed_url_expires_at"] = (
            aws_sdk_dataexchange.types.timestamp.deserialize_json(
                data["SignedUrlExpiresAt"]
            )
        )
    return out
