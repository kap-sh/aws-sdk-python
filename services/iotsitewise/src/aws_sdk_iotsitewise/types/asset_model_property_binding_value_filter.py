"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyBindingValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class AssetModelPropertyBindingValueFilter(TypedDict, closed=True):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model containing the filter property. This identifies the specific asset model that contains the property of interest.</p>"""
    property_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the property within the asset model to filter by. Only data bindings referencing this specific property of the specified asset model are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyBindingValueFilter) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> AssetModelPropertyBindingValueFilter:
    out: AssetModelPropertyBindingValueFilter = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "AssetModelPropertyBindingValueFilter.asset_model_id required"
        )
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    else:
        raise DeserializationError(
            "AssetModelPropertyBindingValueFilter.property_id required"
        )
    return out
