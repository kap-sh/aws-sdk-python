"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromSignedUrlRequestDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093
    import aws_sdk_dataexchange.types.asset_name
    import aws_sdk_dataexchange.types.id


class ImportAssetFromSignedUrlRequestDetails(TypedDict):
    asset_name: "aws_sdk_dataexchange.types.asset_name.AssetName"
    """<p>The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    md5_hash: "aws_sdk_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093.__stringMin24Max24PatternAZaZ094AZaZ092AZaZ093"
    """<p>The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromSignedUrlRequestDetails) -> dict:
    out: dict = {}
    out["AssetName"] = value["asset_name"]
    out["DataSetId"] = value["data_set_id"]
    out["Md5Hash"] = value["md5_hash"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ImportAssetFromSignedUrlRequestDetails:
    out: ImportAssetFromSignedUrlRequestDetails = {}  # type: ignore[typeddict-item]
    if "AssetName" in data:
        out["asset_name"] = data["AssetName"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlRequestDetails.asset_name required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlRequestDetails.data_set_id required"
        )
    if "Md5Hash" in data:
        out["md5_hash"] = data["Md5Hash"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlRequestDetails.md5_hash required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlRequestDetails.revision_id required"
        )
    return out
