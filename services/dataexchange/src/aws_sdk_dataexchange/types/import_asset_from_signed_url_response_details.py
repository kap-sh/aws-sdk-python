"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromSignedUrlResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093
    import aws_sdk_dataexchange.types.asset_name
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.timestamp


class ImportAssetFromSignedUrlResponseDetails(TypedDict, closed=True):
    asset_name: "aws_sdk_dataexchange.types.asset_name.AssetName"
    """<p>The name for the asset associated with this import job.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    md5_hash: NotRequired[
        "aws_sdk_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093.__stringMin24Max24PatternAZaZ094AZaZ092AZaZ093"
    ]
    """<p>The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import response.</p>"""
    signed_url: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The signed URL.</p>"""
    signed_url_expires_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The time and date at which the signed URL expires, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromSignedUrlResponseDetails) -> dict:
    out: dict = {}
    out["AssetName"] = value["asset_name"]
    out["DataSetId"] = value["data_set_id"]
    if "md5_hash" in value:
        out["Md5Hash"] = value["md5_hash"]
    out["RevisionId"] = value["revision_id"]
    if "signed_url" in value:
        out["SignedUrl"] = value["signed_url"]
    if "signed_url_expires_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["SignedUrlExpiresAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["signed_url_expires_at"]
        )
    return out


def deserialize_json(data: dict) -> ImportAssetFromSignedUrlResponseDetails:
    out: ImportAssetFromSignedUrlResponseDetails = {}  # type: ignore[typeddict-item]
    if "AssetName" in data:
        out["asset_name"] = data["AssetName"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlResponseDetails.asset_name required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlResponseDetails.data_set_id required"
        )
    if "Md5Hash" in data:
        out["md5_hash"] = data["Md5Hash"]
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlResponseDetails.revision_id required"
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
