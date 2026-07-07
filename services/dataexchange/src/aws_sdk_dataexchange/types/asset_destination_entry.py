"""Generated from Smithy shape ``com.amazonaws.dataexchange#AssetDestinationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.id


class AssetDestinationEntry(TypedDict, closed=True):
    asset_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the asset.</p>"""
    bucket: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket that is the destination for the asset.</p>"""
    key: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The name of the object in Amazon S3 for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetDestinationEntry) -> dict:
    out: dict = {}
    out["AssetId"] = value["asset_id"]
    out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    return out


def deserialize_json(data: dict) -> AssetDestinationEntry:
    out: AssetDestinationEntry = {}  # type: ignore[typeddict-item]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    else:
        raise DeserializationError("AssetDestinationEntry.asset_id required")
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("AssetDestinationEntry.bucket required")
    if "Key" in data:
        out["key"] = data["Key"]
    return out
