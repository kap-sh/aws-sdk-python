"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromSignedUrlJobErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.asset_name


class ImportAssetFromSignedUrlJobErrorDetails(TypedDict):
    asset_name: "aws_sdk_dataexchange.types.asset_name.AssetName"
    """<p>Details about the job error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromSignedUrlJobErrorDetails) -> dict:
    out: dict = {}
    out["AssetName"] = value["asset_name"]
    return out


def deserialize_json(data: dict) -> ImportAssetFromSignedUrlJobErrorDetails:
    out: ImportAssetFromSignedUrlJobErrorDetails = {}  # type: ignore[typeddict-item]
    if "AssetName" in data:
        out["asset_name"] = data["AssetName"]
    else:
        raise DeserializationError(
            "ImportAssetFromSignedUrlJobErrorDetails.asset_name required"
        )
    return out
