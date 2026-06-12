"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertyBindingValueFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class AssetPropertyBindingValueFilter(TypedDict):
    asset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset containing the property to filter by. This identifies the specific asset instance containing the property of interest.</p>"""
    property_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the property within the asset to filter by. Only data bindings referencing this specific property of the specified asset are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyBindingValueFilter) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> AssetPropertyBindingValueFilter:
    out: AssetPropertyBindingValueFilter = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AssetPropertyBindingValueFilter.asset_id required")
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    else:
        raise DeserializationError(
            "AssetPropertyBindingValueFilter.property_id required"
        )
    return out
