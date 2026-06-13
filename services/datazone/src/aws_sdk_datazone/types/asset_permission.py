"""Generated from Smithy shape ``com.amazonaws.datazone#AssetPermission``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.permissions


class AssetPermission(TypedDict):
    asset_id: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The asset ID as part of the asset permissions.</p>"""
    permissions: "aws_sdk_datazone.types.permissions.Permissions"
    """<p>The details as part of the asset permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPermission) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import aws_sdk_datazone.types.permissions

    out["permissions"] = aws_sdk_datazone.types.permissions.serialize_json(
        value["permissions"]
    )
    return out


def deserialize_json(data: dict) -> AssetPermission:
    out: AssetPermission = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AssetPermission.asset_id required")
    if "permissions" in data:
        import aws_sdk_datazone.types.permissions

        out["permissions"] = aws_sdk_datazone.types.permissions.deserialize_json(
            data["permissions"]
        )
    else:
        raise DeserializationError("AssetPermission.permissions required")
    return out
