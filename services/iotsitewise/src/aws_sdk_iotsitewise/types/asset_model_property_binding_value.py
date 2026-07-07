"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyBindingValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class AssetModelPropertyBindingValue(TypedDict, closed=True):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    property_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model property used in data binding value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyBindingValue) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> AssetModelPropertyBindingValue:
    out: AssetModelPropertyBindingValue = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "AssetModelPropertyBindingValue.asset_model_id required"
        )
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    else:
        raise DeserializationError(
            "AssetModelPropertyBindingValue.property_id required"
        )
    return out
