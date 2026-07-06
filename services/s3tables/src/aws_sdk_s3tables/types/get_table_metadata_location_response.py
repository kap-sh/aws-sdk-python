"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMetadataLocationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.metadata_location
    import aws_sdk_s3tables.types.version_token
    import aws_sdk_s3tables.types.warehouse_location


class GetTableMetadataLocationResponse(TypedDict, closed=True):
    version_token: "aws_sdk_s3tables.types.version_token.VersionToken"
    """<p>The version token.</p>"""
    metadata_location: NotRequired[
        "aws_sdk_s3tables.types.metadata_location.MetadataLocation"
    ]
    """<p>The metadata location.</p>"""
    warehouse_location: "aws_sdk_s3tables.types.warehouse_location.WarehouseLocation"
    """<p>The warehouse location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMetadataLocationResponse) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    if "metadata_location" in value:
        out["metadataLocation"] = value["metadata_location"]
    out["warehouseLocation"] = value["warehouse_location"]
    return out


def deserialize_json(data: dict) -> GetTableMetadataLocationResponse:
    out: GetTableMetadataLocationResponse = {}  # type: ignore[typeddict-item]
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    else:
        raise DeserializationError(
            "GetTableMetadataLocationResponse.version_token required"
        )
    if "metadataLocation" in data:
        out["metadata_location"] = data["metadataLocation"]
    if "warehouseLocation" in data:
        out["warehouse_location"] = data["warehouseLocation"]
    else:
        raise DeserializationError(
            "GetTableMetadataLocationResponse.warehouse_location required"
        )
    return out
