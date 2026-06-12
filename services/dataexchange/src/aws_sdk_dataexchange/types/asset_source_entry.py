"""Generated from Smithy shape ``com.amazonaws.dataexchange#AssetSourceEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string


class AssetSourceEntry(TypedDict):
    bucket: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket that's part of the source of the asset.</p>"""
    key: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The name of the object in Amazon S3 for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetSourceEntry) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["Key"] = value["key"]
    return out


def deserialize_json(data: dict) -> AssetSourceEntry:
    out: AssetSourceEntry = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("AssetSourceEntry.bucket required")
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("AssetSourceEntry.key required")
    return out
